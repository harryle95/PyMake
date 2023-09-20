### PyMake workflow:
- Read `.pymake.toml` config file for config or generate a default. 
- Check for existence of `PyMake.yaml` file
- Read `yaml` file, check for yaml syntax errors
- Classify targets and global variables
- Parse CLI input from invocation, check for parsing errors and build namespace 
- Bind namespace variables to `env` and `cmd`.
- Execute `cmd` and return exit status. 

