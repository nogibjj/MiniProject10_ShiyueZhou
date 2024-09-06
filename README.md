# MiniProject1_ShiyueZhou
[![CI-Python Application Test with Github Actions](https://github.com/nogibjj/MiniProject1_ShiyueZhou/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/MiniProject1_ShiyueZhou/actions/workflows/ci.yml)

Based on the requirement of miniproject in week2, this will work on the following file/folder to develop the Python Template Sample.

requirements.txt
 -->related to packages and version in this project: allows you to specify the exact packages (and versions) to be installed, ensuring consistency across different environments

Makefile
 -->For machine reading and executing by running `make all`.
 -->This sequentially runs `make install`, `make format`, `make lint`, and `make test`.
    install: Installs the required packages listed in `requirements.txt`.
    format: Formats the code to ensure it follows proper code style (using black).
    lint:  Runs a linter tool (pylint) to analyze the source code for programming errors, bugs, stylistic issues, and coding standard violations. Ensures code follows best practices and is free of common mistakes before being committed or deployed.practices and is free of common mistakes before it is committed or deployed.
    test: Uses pytest to run the test files, ensuring the code works as expected.
    all: Runs all the above tasks sequentially (install, format, lint, test).

Dev Container
    The ".devcontainer" folder contains two parts: 
    devcontainer.json: This is the main configuration file that defines the development container’s setup, specifying the tools, settings, and extensions for the environment.
    Dockerfile: Defines a custom Docker image used to create the container. It specifies the base image and any additional dependencies or system configurations required for the development environment.

Github Actions  
    The directory .github/workflows is where you define your workflows for GitHub Actions.
