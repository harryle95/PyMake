# PyMake

## Installing PyMake:

```commandline
pip install PythonMake
```

## What this program is about:

A wrapper that allows you to run multiple commands/scripts with variables that can be provided through CLI.

To run PyMake, you will need to create a `PyMake.yaml` file and define a make target recipe. The general structure of 
a `PyMake.yaml` is: 

```yaml
target:
    var:
      basic: [var1, var2, var3]
      option: {opt1: flag1, opt2:flag2, opt3:flag3}
      sequence: [list1, list2]
    env: {ENV1: "value1", ENV2: "value2"}
    cmd:
      - command1
      - command2
```

## To run a target:

```commandline
pymake run <target> <arguments>
```

# Quick start:

## A `Hello World` example:

```yaml
# PyMake.yaml
hello:
    cmd:
        - echo "Hello World"
```
The make file defines the target `hello`. Executing `hello` requires running the command `echo "Hello World"`

```bash
pymake run hello
```

## Add and Commit 