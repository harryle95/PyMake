### Reserved keywords:
`basic, option, sequence` are reserved keywords, which means you cannot have variable with the same name as the reserved
keyword. However, the reserved keywords are case-sensitive, which means `Basic`, `Option`, `Sequence` are valid variables.

### Type mapping:

``` python
simple_type = int | float | bool | str
simple_reference = '${{ expr }}'
reference_type = simple_reference| str + simple_reference + str
default_non_null = simple_type | reference_type
default = default_non_null | None 
default_sequence = default | list[default_non_null]

```

Simple type includes variable that is either a string or a python non-container type (does not have the `__len__` attribute).
Reference type is a string with an expression enclosed by `${{}}` whose value is expanded at run time. Default type is either 
simple type or a reference type, which may or may not take None value (default_non_null cannot be None). Default sequence
is a default variable or a list of default_non_null variables. 

### Under the type element:

```yaml
target:
    var:
        basic:
            basic_var: default # variables can have a default value or undeclared
            null_var: # variable without default = required 
            reference_var: ${{basic_var}}/${{null_var}} # variable referencing the value of other variables
        option:
            optional_var: default_non_null # option variable cannot be null
        sequence:
            sequence_var: default_sequence
            null_sequence: # sequence var without default is also permitted
```

### Outside the type element - dictionary style:
```yaml
target:
  var:
    var1: default # variables declared under var is basic by default
    var2: # Inline declaration to add default and type information
      default: default_non_null
      type: option 
    var3: # Inline declaration without default field set default to null (var is required)
      type: sequence
```

### Outside the type element - list style:
```yaml
target:
  var:
    - var1 # default = null, type = basic 
    - var2: # default = null, type = sequence
        type: sequence
    - var3: # default = default, type = basic 
        default: default
        type: basic
```

### Hybrid - list style:

```yaml
target:
  var:
    - var1
    - var2
    - basic: [b1, b2, b3]
    - option: [o1, o2, o3]
    - sequence: [s1, s2, s3]
```

### Hybrid - dict style:

```yaml
target:
  var:
    var1:
    var2:
    - basic: [b1, b2, b3]
    - option: [o1, o2, o3]
    - sequence: [s1, s2, s3]
```



## Understand PyMake variables:

Each pymake variable is an object containing the following fields:

- value
- position
- type 
- default 
- required
- need_expansion

`type` is the variable type, which takes the value of the type element the value is declared under, the explicit type declaration 
using the `type` field if the variable is declared directly under `var`, 
or `basic` by default. 

`default` is the default value provided at declaration, which can be `null` or unprovided (evaluated to `null` by yaml).

`required` is a calculated field based on the value of `default`. If `default` value is provided, `required` is False and 
vice versa. 

`position` determines the variable's position when positional parameters are parsed. Only `basic` type variables can take 
positional value.

`value` and `need_expansion` are determined at runtime. If a value is passed to the variable at invocation, the `value` field is set to value,
and `need_expansion` is set to False. If a value is not passed and default is a `reference_type` (i.e. contains `${{}}`), 
`need_expansion` is set to True. A variable with `need_expasion` = True will be evaluated after its reference is evaluated. 
If circular referencing is detected, a `CircularReferencingError` is raised.

At the `build` stage, pymake determines the value of `type`, `default`, `required`, and `position`. At the `parse` stage,
`pymake` determines the value of `value` and `need_expansion`. The binding process, if proceeded without error, returns a 
namespace of {`variable_name`: `value`} that is used to expand environment variables and commands. 

