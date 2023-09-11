# PyMake
A more convenient way to run Python and CLI

# Quick example:

## Running a simple command with user input arguments
```
script:
    var: [var1, var2]
    cmd:
        - python3 script.py --arg1=$(var1) --arg2=$(var2)
```

Users can invoke the target as follows:

```
pymake script --var1 10 --var2 100
```

Or alternatively:

```
pymake script 10 100
```

This is equivalent to invoking the command:

```
python script.py --arg1=10 --arg2=100
```

## Running Pytest with custom target:
```
test:
    var:
        - test_item: ""
    cmd:
        - poetry run pytest path/to/tests/$(test_item)
```

Users can invoke the following command to test all files in "path/to/tests/":

```
pymake test
```

Or run all tests in a specific test dir located in `path/to/tests/dir`:

```
pymake test dir
```

## Setting up environment variables to provide a runtime environment for cmd:
```Python
#script.py
import os
import argparse

# Reading password from environment variables
password = os.environ["PASSWORD"]

# Reading other connection info from CLI
parser = argparse.ArgumentParser()
parser.add_argument("--host", type=str)
parser.add_argument("--port", type=int, default=8000)
parser.add_argument("--usr", type=str)
args = parser.parse_ars()

# Print out results for demo
print(f"Connecting to {args.host} at port: {args.port}, under: {args.usr} with password: {password}")
```

We can write a PyMake file as follows:

```
script:
    var:
        - host: localhost
        - port: 8000
        - usr: testuser
        - password: 123456
    env:
        - PASSWORD: $(password)
    cmd:
        - python script.py --host=$(host) --port=$(port) --usr=$(usr)
```

We can invoke the target `script` as follows:

```
pymake script 127.0.0.1 8080 --password $(MYSECRETPASSWORD)
```

Pymake will make a runtime environment with PASSWORD set as an environment variable with value $(MYSECRETPASSWORD). Pymake then execute the command inside this environment. Assuming `MYSECRETPASSWORD=Password@123456`, the result for running the previous command is:

```
Connecting to 127.0.0.1 at port: 8000, under: testuser with password: Password@123456"
```

## Running multiple Python scripts at once:

```
script:
    var:
        - arg1: default1
        - arg2: default2
        - arg3: default3
        - arg4: default4
        - env: defaultenv
    env:
        - ENV_VAR: $(env)
    cmd:
        - python script1.py arg1 arg2
        - python script2.py arg3 arg4
```
