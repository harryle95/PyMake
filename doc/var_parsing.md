## Understand PyMake variable parsing 

Variables can be parsed as positional arguments or keyword arguments. Any local namespace's variable can be keyword declared 
using the `--<variable> <arg>` construct. For instance, given the following target, 

```yaml
#PyMake.yaml
echo_msg:
  var: message
  cmd: echo ${{message}}
```
We can invoke `pymake run echo_message --message "Hello World"` to print out to stdout `Hello Wordl`. The string value 
"Hello World" is bound to the variable message at parsing. 

Variable types determine how many arguments the variable can take, whether the variable can parse positional arguments, and 
whether default value must be provided. The rules are: 

- `basic` variables can take positional argument, based on the order they are declared w.r.t to all positional arguments. 
`basic` variables can only take one value, either via keyword or positional arguments, and basic variables does not always
need to have default value declared. 
- `option` variables can only be activated using keyword argument and does not take any command line value. Default value for 
an option variable must be provided. 
- `sequence` variables can only be activated using keyword argument and take at least one position argument after the keyword 
is parsed. Sequence variables can be defaulted to null, making them required. 

## Parsing rule:

- Parse variables from left to right
- Until the first keyword is detected using the `--<varname>` syntax:
  - Positional arguments are bound to basic variables based on their respective position.
  - Raise an error if all variables that can take positional arguments are exhausted.
- If a keyword `--<varname>` is detected:
  - If variable `varname` is `basic`, bind the next argument (must be position) to its value.
    - If the next argument is not positional or the argument after the bound value is not a keyword argument, raise an error.
  - If variable `varname` is `option`, proceeds to the next argument. If the next argument is positional, raise error.
  - If variable `varname` is `sequence`, bind the next series of positional argument to its value. Only stop when a keyword argument 
  is detected. 

An implication of this is variable can be defined in any order. The only time when order is taken into account is when 
positional argument is parsed. However, once a keyword argument is specified, positional binding is no longer applied. 
If a variable is bound multiple times, an error is raised. 

### Example:

```yaml
calculate:
  var:
    basic:
      message: "Hello World"
      task: "calculating sum"
      length: ${{len(values.split()}}
    sequence:
      values: [1, 2, 3, 4, 5]
    cmd:
      - echo ${{message}}
      - echo "The current task is ${{task}} of ${{length}} numbers"
      - |
        #!/usr/bin/python3.11
        array = [int(i) for i in ${{values}}.split()]
        print(sum(array))
```

In this example, we are printing a greeting message, then printing a message to describe the task to perform, then calculating 
the sum and printing out the result. If we invoke the target as follows: 

```commandline
pymake run calculate
```
The result is 
```commandline
Hello World
The current task is calculating sum of 5 numbers
15
```

We can parse values to the basic variables in a positional manner as follows, all of which returns the same result.

```commandline
pymake run "Hello World" "calculating sum" 5
pymake run "Hello World" "caculating sum" --length 5
pymake run "Hello World" --task "caculating sum" --length 5
pymake run --message "Hello World" --task "calculating sum" --length 5 
pymake run "Hello World" --length 5 --task "caculating sum"
pymake run --task "calculating sum" --length 5 --message "Hello World" 
```

If we want to parse the value of `values`:

```commandline
pymake run "Hello World" "calculating sum" --values 1 2 3 4 5
pymake run "Hello World" "caculating sum" --values 1 2 3 4 5 --length 5
pymake run "Hello World" --values 1 2 3 4 5 --task "caculating sum" --length 5
```

Whereas the following invocation will return an error: 
```yaml
pymake run "Hello World" --message "hello world" # Variable message bound multiple times
pymake run "Hello World" --task --length 5 # Variable task expects a value which is not provided
pymake run "Hello World" --task "calculating sum" 5 # Once a keyword argument is specified, basic variable can no longer be parsed as positional 
```
