
## How are variables expanded:

Each pymake target can access the static namespace, consisting of environment variables accessible via the current shell, 
the global namespace consisting of globally declared variables in PyMake file, and the local namespace, consisting of variables
declared under the target and parsed at invocation. Whenever an expression is evaluated using `${{}}`, the variables in the expression
are first expanded using the local namespace. If some variables are not present in the local namespace, a global namespace and 
static namespace is subsequently looked up. If the variable cannot be expanded after the previous step, a variable not found 
error is returned. 

### Example: local over global:

```yaml
#PyMake.yaml
var1: 10

target:
  var:
    var1: 1000
  cmd:
    echo ${{var1}}
```

The result after invoking `pymake run target`

```commandline
1000
```
Here `var1` is expanded to the value in the local namespace, taking the default value 1000.

### Example: global over static:
```
#PyMake.yaml
var1: 10

target:
  cmd:
    echo ${{var1}}
```
If before calling `pymake run target`, we do `export var1=1000`, the result after running `pymake run target` is

```commandline
10
```

### Example: referencing static variable:
```
#PyMake.yaml
target:
  cmd:
    echo ${{var1}}
```

Here, `var1` is not defined in the local or global namespaces. pymake will attempt do call 
`os.getenviron("var1")` to get the `var1` value. If this does not work, a `VariableNotFound` error will be raised. 
