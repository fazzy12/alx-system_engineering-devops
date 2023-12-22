# API Python Scripting

## Overview

This project focuses on utilizing Python scripting to interact with a REST API that provides employee data. The goal is to extract, organize, and export this data into different formats such as CSV and JSON. The project aims to highlight the limitations of Bash scripting in certain scenarios and demonstrate the efficiency of Python for such tasks.

## Purpose

The primary objective of this project is to familiarize participants with:

- Python scripting for data extraction and manipulation
- Understanding and working with REST APIs
- Data export to different formats like CSV and JSON
- Code organization and adherence to industry standards

## Background Context

Traditional system administrators typically rely on Bash scripting for automation tasks. However, as systems grow more complex, there is a need for a more robust and efficient approach. This project emphasizes the importance of Python scripting, particularly for interacting with APIs and managing data structures.

## Learning Objectives

Upon completing this project, participants should be able to:

- Understand the limitations of Bash scripting for certain tasks
- Define and explain what an API is, particularly REST APIs
- Understand the concept of microservices
- Work with data formats like CSV and JSON in Python
- Adhere to Pythonic coding styles and standards

## Requirements

### General

**Allowed Editors**: vi, vim, emacs
**Platform**: Ubuntu 20.04 LTS with Python 3.8.5
**Code Style**: pycodestyle (version 2.8.\*)
**Documentation**: All modules should have proper documentation
**Error Handling**: Use `get` method for dictionary access
**File Headers**: All files should start with `#!/usr/bin/python3`

## Tasks

Task 0: Gather Data from an API

- **Objective**: Extract and display TODO list progress for a given employee ID.
- **Tools**: Use `urllib` or `requests` module.

Task 1: Export to CSV

- **Objective**: Extend the previous task to export data in CSV format.
- **File Format**: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

Task 2: Export to JSON

- **Objective**: Extend the previous tasks to export data in JSON format.
- **File Format**: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}

Task 3: Dictionary of list of dictionaries

- **objective**: Records all tasks from all employees
- **File Format**: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}

## Resources

- [Friends don’t let friends program in shell script](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script)
- [What is an API?](https://www.webopedia.com/definitions/api/)
- [What is a REST API? English please](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)
- [what is a REST API](https://www.sitepoint.com/rest-api/)
- [What are microservices?](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)
- [PEP8 Python style](https://peps.python.org/pep-0008/)

## Contact

For any questions or feedback, please contact:

[Ifeanyi kalu](https://www.linkedin.com/in/ifeanyi-kalu)



