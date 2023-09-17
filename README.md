# PyMake

## Installing PyMake:

```commandline
pip install PythonMake
```

## What this program is about:

PyMake is a wrapper that allows you to run multiple commands/scripts with variables that can be provided through CLI.

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
`var` element defines all variables in the namespace local to `target`. The variables
can be used to interpolate environment variables or command referencing them via the syntax `$(var)`. 

`basic` variables are variables that take exactly one value. `basic` variables can take on default (single) values. A 
`null` value means that the variables must be defined at run time. `basic` variables can be parsed as positional arguments
or by using keyword argument: `--<varname> value`.

`option` variables take no value but is used to activate the corresponding 
option in `cmd`. The default value provided for each `option` variable specifies how the corresponding option will be
raised in `cmd`. If an `option` variable is not set at `pymake run`, it will not be triggered in the referencing commands.
`option` variables can be activated using `--<varname>`.

`sequence` variables are variables that take on at least one value. `sequence` variables can also take on default values,
and a `null` default value means that the variable must be provided at `pymake run`. `sequence` variable can only be defined
using `--<varname> value1 value2 ...`.

`env` element defines all environment variables. Environment variables will be defined in the shell used to execute the commands.
Environment variables can be set using `key: value` pairs, where value is a hard-coded value, or is a reference to a `var`
variable in this format: `key: $(var)`. Note that a reference is not restricted to a single variable. The following definition
is valid:

```yaml
env:
    url: "http://$(hostname):$(port)"
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

## Add and Commit example
```yaml
commit:
    var:
        basic:
            message: null
        option:
            interactive: "-i"
            verbose: "-v"
            dryrun: "--dry-run"
        sequence:
            pathspec: .
    cmd:
      - git add -A $(verbose) $(interactive) $(pathspec)
      - git commit $(verbose) $(dryrun) --message "$(message)"
```
Acknowledging that you can do pretty much the same thing with every IDE, I just want to show how PyMake can simplify
this add to commit git workflow. Note that here you have to add in the quotation marks yourself. 

### To add a specific file: 
```commandline
pymake run commit "feat: add a new target in PyMake.yaml" --pathspec PyMake.yaml
```

### To add all files
```commandline
pymake run commit "feat: update current repository"
```

### To do a dryrun 
This checks which files are to be committed but does not actually commit. 

```commandline
pymake run commit "feat: do a dry run" --dryrun
```