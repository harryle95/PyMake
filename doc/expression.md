### `${{expr}}` expression 

Can be used to interpolate a variable value, an if else statement. 

#### Value Evaluation: 

Value evaluation means returning a value from evaluating the expression inside ${{}}. Pymake 
allows users to write valid python expressions in value evaluated statements. Valid here means that 
you can pass the expression to `eval` in python and receive a matching response. For example, to declare 
the following variables using the `${{}}` expression is valid:

```yaml
#PyMake.yaml
GRADING_SCHEME:
  pass: 5
  
doPass:
  var:
    name: ${{"Harry"}} # name = Harry
    grades: ${{[grade for grade in range(10)]}} # grades = [1, 2, ..., 10]
    pass: ${{sum(grades)/len(grades) >= GRADING_SCHEME.pass}} # Check whether the average of grades is >= 5 
  ...
```

#### Conditional Evaluation: 

Conditions are specified under the `cmd` element, using this syntax: 

```yaml
cmd:
  - ${{if expr}}:
      <commands>
    ${{elif expr}}: 
      <command>
    ${{else}}:
      <command>
```

pymake will evaluate the circuit sequentially from if to elif to else, executing the commands on the branch that is first 
evaluated to True.

