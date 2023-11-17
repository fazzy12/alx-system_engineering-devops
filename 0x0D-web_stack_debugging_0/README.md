<div style="width: 100%; height: 0; padding-bottom: 50%; position: relative;">
    <img src="uWLzjc8.jpg" alt="OOP Image" style="position: absolute; width: 800%; height: 100%; object-fit: cover;">
</div>

# Web Stack Debugging Project - Level 0

## Description

The goal of this project is to debug a web stack by resolving issues that prevent Apache from serving a page containing "Hello Holberton" when querying the root of the server.

## Concepts

This project covers the following concepts:

- Network basics
- Docker
- Web stack debugging

## Background Context

Debugging is a crucial skill for Full-Stack Software Engineers, as it allows them to identify and fix issues in a web stack. The project provides a broken/bugged web stack, and the objective is to manually fix the issues and then create a Bash script that automates the debugging steps.

## Example Scenario

### Given Information

A server must have a copy of the `/etc/passwd` file in `/tmp` and a file named `/tmp/isworking` containing the string "OK" for the web application to work.

### Debugging Steps

```
docker run -d -ti ubuntu:14.04
docker exec -ti <container_id> /bin/bash
cp /etc/passwd /tmp/
echo OK > /tmp/isworking
```

###  Docker Installation
For this project, you will be given a container to solve the task. If you want to install Docker on your local machine or VM, you can follow the installation instructions for:

- [Mac OS]()
- [Windows]()
- [Ubuntu 14.04]()
- [Ubuntu 16.04]()

### Requirements
- Allowed editors: `vi, vim, emacs`
- All files interpreted on `Ubuntu 14.04 LTS`
- All files end with a new line
- `README.md` file at the root of the project folder is mandatory
- Bash script files must be executable
- Bash scripts must pass `Shellcheck` without any error
- Bash scripts must run without error
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining the script's purpose

### Tasks
- **Task 0: Give me a page!**

In this task, the goal is to get Apache to run on the container and return a page containing "Hello Holberton" when querying the root of the server.

### Example:
```
docker run -p 8080:80 -d -it holbertonschool/265-0
curl 0:8080
```

After connecting to the container and fixing the issues, running the curl command should return the expected page. Paste the command(s) used to fix the issue in your answer file.

Copyright © 2023 ALX, All rights reserved.

