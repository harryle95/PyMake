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