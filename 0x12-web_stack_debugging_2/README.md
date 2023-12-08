# Web Stack Debugging 2

## Overview

This project focuses on web stack debugging and DevOps practices. The tasks involve fixing configurations and optimizing the setup of an Nginx web server to enhance security and performance.

## Table of Contents

- [Tasks](#tasks)
  - [Task 0: Run Software as Another User](#task-0-run-software-as-another-user)
  - [Task 1: Run Nginx as Nginx](#task-1-run-nginx-as-nginx)
  - [Task 2: 7 Lines or Less](#task-2-7-lines-or-less)
- [Scripts](#scripts)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Tasks

### Task 0: Run Software as Another User

The script in `0-iamsomeoneelse` allows running the `whoami` command under a specified user, promoting better security practices by avoiding direct execution as the root user.

### Task 1: Run Nginx as Nginx

The script in `1-run_nginx_as_nginx` configures Nginx to run as the `nginx` user, listening on port 8080. This enhances security by avoiding the default configuration of running web servers as the root user.

### Task 2: 7 Lines or Less

The script in `100-fix_in_7_lines_or_less` optimizes the Nginx configuration script, achieving the same results with brevity and readability within 7 lines.

## Scripts

- `0-iamsomeoneelse`: Script for Task 0.
- `1-run_nginx_as_nginx`: Script for Task 1.
- `100-fix_in_7_lines_or_less`: Optimized script for Task 2.

## Usage

1. Clone the repository:

   ```
    git clone https://github.com/your-username/alx-system_engineering-devops.git
    ```

2. Navigate to the project directory:


    ```
    cd alx-system_engineering-devops/0x12-web_stack_debugging_2
    ```

3. Run the scripts:

    ```
    ./0-iamsomeoneelse <username>
    ./1-run_nginx_as_nginx
    ./100-fix_in_7_lines_or_less
    ```
### Contributing

Contributions are welcome! Feel free to open `issues` or `pull requests`.