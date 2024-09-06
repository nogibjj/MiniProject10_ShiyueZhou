# MiniProject1_ShiyueZhou
[![CI-Python Application Test with Github Actions](https://github.com/nogibjj/MiniProject1_ShiyueZhou/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/MiniProject1_ShiyueZhou/actions/workflows/ci.yml)

Based on the requirement of miniproject in week2, this will work on the following file/folder to develop the Python Template Sample.  

# requirements.txt<br>
 -->related to packages and version in this project: allows you to specify the exact packages (and versions) to be installed, ensuring consistency across different environments  

# Makefile<br>
 -->For machine reading and executing by running `make all`.  
 -->This sequentially runs `make install`, `make format`, `make lint`, and `make test`.   
- **install**:: Installs the required packages listed in `requirements.txt`.  
- **format**:: Formats the code to ensure it follows proper code style (using black).  
- **lint**: Runs pylint to analyze the code for potential errors, coding standard violations, and best practices. 
- **test**: Uses pytest to run the test files, ensuring the code works as expected.  
- **all**: Runs all the above tasks sequentially (install, format, lint, test).  
 
  
# Dev Container<br>
 The `.devcontainer` folder contains two key components:
- **`devcontainer.json`**: The main configuration file that defines the development container’s setup. It specifies the tools, settings, and VSCode extensions for the environment.
- **`Dockerfile`**: Defines a custom Docker image used to create the container. It specifies the base image and any additional dependencies or system configurations required for the development environment.



# Github Actions<br>
 The `.github/workflows` directory contains workflows that automate various tasks using GitHub Actions.  

1. **`name: CI Pipeline`**  
   This gives the workflow a name, which will appear in the GitHub Actions tab of your repository.  

2. **Triggers (`on`)**:  
   - **`push`**: The workflow is triggered when code is pushed to the `main` branch.  
   - **`pull_request`**: The workflow is triggered when a pull request is opened or updated for the `main` branch.  

3. **Jobs (`jobs`)**:  
   - **`build`**:  
     - **`runs-on`**: This specifies the environment (runner) where the job will run. GitHub provides hosted runners, and in this case, it uses the latest version of Ubuntu (`ubuntu-latest`).  
     - **`steps`**: Each job contains a series of steps. Steps are the individual tasks performed in sequence, such as checking out code, installing dependencies, linting, and running tests.


## Check:
![requirements](image.png)
