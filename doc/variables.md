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
at invocation, by passing positional or keyword arguments through the command line. 
Any variable declared under `var` can be parse as a keyword via the `--<varname>` construct.

For instance, any of the following invocations are acceptable:

```commandline
pymake run target localhost 8080 testdb
pymake run target --hostname localhost --port 8080 --database testdb
pymake run target localhost --port 8080 --database testdb 
pymake run target localhost 8080 --database testdb 
pymake run target --port 8080 --database testdb --hostname localhost 
```
Any of the previous invocations will bind the value `localhost` to `hostname`, `8080` to `port` and `testdb` to `database`.

#### Local variable type declaration:

Local variables can be a `basic`, `option`, or `sequence` type. The main difference between the three types is how pymake 
bind variables at parsing. Variables can be declared under the corresponding element. For instance, 

```yaml
#PyMake.yaml 
target:
  var:
    basic:
      b1: 10
      b2: 10
    option:
      o1: '-a'
      o2: '-b'
    sequence:
      s1: [1, 2, 3]
      s2: [4, 5, 6]
  ...
```
Here, `b1, b2` are basic variables, `o1, o2` are option variables, and `s1, s2` are sequence variables.

Variables can also be declared directly under `var`. The following definition is equivalent to the previous:

```yaml
#PyMake.yaml
target:
  var:
    b1: 10
    b2: 10
    o1:
      value: -a
      type: option
    o2:
      value: -b
      type: option
    s1:
      value: [1, 2, 3]
      type: sequence
    s2:
      value: [4, 5, 6]
      type: sequence
```

Note that you can also do a mix and match between the two styles. For more information on local namespace variable declaration
and parsing, please refer to [this page](var_declaration.md)



### Global Namespace

#### Declaration

Global variables can be declared inside the `PyMake.yaml` file using the `key: value` format, where value can contain any
keyword except for `cmd`, which is reserved to distinguish between a variable and a keyword. The following declarations are
all valid:

```yaml
BASE_VERSION: 3.10 # Float value

DEFAULT_PYTHON: /usr/bin/ # String Value

PYTHON_ENVS: # List of String value
  _ /home/user/venv/bin/python
  - /home/user/torch_env/bin/python
  - /home/user/sklearn_env/bin/python

MYSQL_INFO: # Dictionary value
  address: 172.0.0.1
  port: 1433
  database: testdb
  usr: db_user

```
The convention recommended by pymake is to have global scoped variables in upper case and local scope variables in lower case.
This convention is not strictly enforced but is highly recommended. 

#### Referencing 

Global variables can be expanded using `${{}}` expression. Simple-value typed global variables can be referenced using its name.
Dictionary-typed global variables can only be referenced using its attribute. Using the previous example, we 
can reference `${{BASE_PYTHON}}, ${{DEFAULT_PYTHON}}, ${{PYTHON_ENVS}}` but we can only reference 
MYSQL_INFO with its attributes: `${{MYSQL_INFO.address}}, ${{MYSQL_INFO.port}}`



### Static namespace

Static namespace consists of environment variables that the current shell can access. Static namespace variables are often
set automatically via the `export` shell command.


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


