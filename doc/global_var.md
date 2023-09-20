
## Global Variables

### Declaration

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

### Referencing 

Global variables can be expanded using `${{}}` expression. Simple-value typed global variables can be referenced using its name.
Dictionary-typed global variables can only be referenced using its attribute. Using the previous example, we 
can reference `${{BASE_PYTHON}}, ${{DEFAULT_PYTHON}}, ${{PYTHON_ENVS}}` but we can only reference 
MYSQL_INFO with its attributes: `${{MYSQL_INFO.address}}, ${{MYSQL_INFO.port}}`


