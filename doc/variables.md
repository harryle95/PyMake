## Overview 

Pymake uses the concept of namespace to execute target. Namespace defines a set of variables that target commands and
environment can access at run time. Each container has 

- a **local** namespace defined using the `var` element inside a target.
- a **global** namespace defined using global declarations inside `PyMake.yaml` file.
- a **static** namespace of environment variables declared outside of `pymake` -i.e. environment variables that your current shell has access to.

### Local namespace

#### Namespace declaration

Local namespace consists of variables declared under the `var` element inside a target. For instance,

```yaml
#PyMake.yaml
target:
    var:
      basic: [hostname, port, database]
    ...
```
The target's namespace consists of three variables `hostname, port, database`. The variables defined in the local namespace
can be referenced by items in `env` or `cmd` elements. 

#### Invoking target with namespace variables

A distinct feature of pymake is local variables can be defined dynamically
at invocation, by passing positional or keyword arguments through the command line. For instance, any of the following invocations are acceptable:

```commandline
pymake run target localhost 8080 testdb
pymake run target --hostname localhost --port 8080 --database testdb
pymake run target localhost --port 8080 --database testdb 
pymake run target localhost 8080 --database testdb 
pymake run target --port 8080 --database testdb --hostname localhost 
```
Any of the previous invocations will bind the value `localhost` to `hostname`, `8080` to `port` and `testdb` to `database`.
Refer to [this]() for more information on local variable namespace definition, invocation and binding. 

### Global namespace 

Global variable can be declared using a `key:value` construct native to `yaml`. Value can be a simple value like an int or 
a string, but also can be an object if parsed like a dict. The distinction between `variable` and `target` is `variable` cannot 
have a `cmd` element.

### Static namespace

Static namespace consists of environment variables that the current shell can access. 


## Run-time environment setup 

After parsing through invocation, the run-time environment is setup to execute commands defined in `cmd`. This involves
populating the run-time environment with environment variables declared under `env`. Environment variables are declared using 
the `key: value` construct, where value can be a user-set value or a referenced variable that is expanded at run-time. At run-time,
`key` is the identifier of the newly set environment variable, while `value` is the value. This is akin to doing 
`os.environ[key]=value`. 

```yaml
#PyMake.yaml
print_env:
  env:
    MYENV: 10
  cmd:
    echo $MYENV
```

Running `pymake run print_env` will show this on the screen:
```
10
```

As mentioned previously, environment variable can also reference another variable, either a local or a global namespace 
variable: 

```yaml
#PyMake.yaml
PORT: 8080

print_env:
  var:
    basic:
      localhost: 172.0.0.1
  env:
    HOST: ${{localhost}}
    PORT: ${{PORT}}
  cmd:
    echo $HOST $PORT
```

Running `pymake run print_env localhost` will show this on the screen:
```
localhost 8080
```

Running `pymake run print_env` will display:
```
172.0.0.1 8080
```



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
