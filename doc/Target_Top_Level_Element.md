# var

Represents variables that can be entered from the CLI. `var` allows users to interract with the target build environment, setting variables to be used for commands or setting up runtime environment.

## var types

There are three types of variables:

- Basic Variables: of type `int`, `float`, `string`, `boolean` that expect exactly one value followed.
- Flag Variables: used for setting options. Do not expect any value.
- Array Variables: of type `list`. Expect at least one value to follow.

## Basic variables

### As required arguments

Flow style:

```
#PyMakefile

target:
    var:
        basic: [var1, var2, var3]
```

Block style:

```
#PyMakefile

target:
    var:
        basic:
            - var1
            - var2
            - var3
```

### With default values:
Flow style:

```
#PyMakefile

target:
    var:
        basic: {var1: 10, var2: 20, var3: 30}
```

Block style:

```
#PyMakefile

target:
    var:
        basic:
            var1: 10
            var2: 20
            var3: 30
```

### Interleaved: some positional, some required

The only permitted way is Block style, with all required arguments listed first, followed by optional arguments with default value:

```
#PyMakefile:
target:
    var:
        basic:
            var1: REQUIRED
            var2: 20
            var3: 30
```

Here `var1` is a required variable, and `var2`, `var3` are optional.

## Flag variables

Flag variables are associated with variables defined with `set_action="stored_true"` in Python `argparse` or option flag bits in bash command - i.e. `ls -a`. Flag variables are defined as follows:

```
#PyMakefile
ls:
    var:
        flag:
            long: -l
            all: -a
            recursive: -R
    cmd:
      - ls $(long) $(all) $(recursive)
```

Here `long`, `all`, `recursive` are the options that can be passed to the standard unix command `ls`. The value associated with each flag defines how they will be entered into the command that uses those flags. For instance, invoking:

```
pymake ls --long
```

is equivalent to invoking
```
ls -l
```

If a flag is not called at invocation, it will not be injected into the coresponding command. For instance, invoking

```
pymake ls --long --all --recursive
```

is equivalent to

```
ls -l -a -R
```

where as

```
pymake ls
```

is equivalent to

```
ls
```

## List variables

List variables are associated with parser arguments with `nargs="+"`. Similar to basic variables, list variables can be defined in flow style or block style. When defining list variables with default value, it is recommended to use block style with default value set as Python list:

```
#PyMakefile

target:
    var:
        list:
            var1: REQUIRED
            var2: [4,5,6]
    cmd:
        - python script.py --list_val1 $(var1) --list_val2 (var2)
```

In this example, `var1` is a required parameter while `var2` is optional. If `target` is invoked with the following command:

```
pymake target --var1 1 2 3
```

The program will run

```
python script.py --list_val1 1 2 3 --list_val2 4 5 6
```
Note that list variables can only be entered using keyword arguments. Also note that if you are using list variable in the CLI, the correct way is

```
python script.py --list_val1 $(var1) --list_val2 (var2)
```

Not
```
python script.py --list_val1=$(var1) --list_val2=$(var2)
```

## How var variables are parsed from CLI input

By default, any variable defined in `var` can be defined with a matching flag. Depending on the variable type, input will be parsed, coerced, and associated with the variable.

### Basic variable:

```
# PyMakefile
target:
    var:
        basic: [var1, var2]
    ...
```

We can run the target as follows:

```
pymake target --var1 10 --var2 100
```

Or

```
pymake target 10 100
```

Or

```
pymake target 10 --var2 100
```

In this example, the value 10 is associated with `var1` and 100 with `var2`. Basic variable is the ONLY variable type that can be entered as positional arguments. Positional values are assigned to basic variables by the order of definition (10 -> `var1`, 100 -> `var2`).

Variables can also be defined with default values:

```
# PyMakefile
target:
    var:
        basic:
            - var1: 10
            - var2: 100
    ...
```

We can execute target by calling:

```
pymake target --var1 1000
```

Or

```
pymake target 1000
```

In this case, the value 1000 is entered as a positional argument and is matched with `var1`. No value is entered for `var2` and hence is assigned 100 by default.

### Common Errors at Invocation

Referring to the previous example, we will show some ways in which parsing exceptions can occur:

#### Positional after keyword

```
pymake target --var1 100 1000
```

The only time this is a valid syntax is when `var1` is a `list` type variable. This will raise a `PositionalFollowedByKeyword` exception.

#### Multiple definitions

The following invocations will raise a `MultipleDefinitions` exception:

```
pymake target 10 --var1 100
```

Or

```
pymake target --var1 10 --var1 100
```

#### Undefined variable:

```
pymake target -var5 10
```
This will raise a `UndefinedVariable` exception.

#### Missing required variables:

Referring to this example:

```
# PyMakefile
target:
    var:
        basic: [var1, var2]
    ...
```

Since we do not provide default values for `var1` and `var2`, they are expected. Invoking target the following ways will raise `MissingRequiredVariable` exceptions:

```
pymake target
```

Or
```
pymake target 10
```
