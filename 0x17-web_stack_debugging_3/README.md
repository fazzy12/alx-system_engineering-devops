# Web Stack Debugging Project: Fixing Apache 500 Error

## Overview

Welcome to the Web Stack Debugging Project, where we tackle real-world challenges in managing and troubleshooting web stacks. In this project, we focus on debugging and fixing an Apache 500 error on a WordPress website running on a LAMP stack.

### Project Goals

- Use `strace` to identify the root cause of the Apache 500 error.
- Fix the identified issue manually.
- Automate the fix using Puppet.
- Ensure the WordPress website is running smoothly without any errors.

## Technologies Used

- Ubuntu 14.04 LTS
- Apache
- MySQL
- PHP
- WordPress
- Puppet

## Project Structure

- `0-strace_is_your_friend.pp`: Puppet manifest file containing the code to automate the fix for the Apache 500 error.
- `README.md`: This document providing an overview of the project and instructions for setup and usage.

## Setup and Usage

### Prerequisites

- Ensure you have Ubuntu 14.04 LTS installed.
- Install Puppet and `strace`:

  ````
  $ apt-get install -y ruby
  $ gem install puppet-lint -v 2.1.1
  ```

### Instructions

1. Clone the repository:

```
$ git clone https://github.com/your-username/alx-system_engineering-devops.git
$ cd alx-system_engineering-devops/0x17-web_stack_debugging_3
```
2. Update the Puppet manifest (`0-strace_is_your_friend.pp`) with the correct paths for your system.

3. Apply the Puppet manifest to automate the fix:

```
$ puppet apply 0-strace_is_your_friend.pp
```
4. Verify that the Apache 500 error is resolved and the WordPress website is functioning correctly.

### Conclusion
This project provides hands-on experience in debugging web stack issues and automating fixes using configuration management tools like Puppet. By following the instructions and applying the Puppet manifest, you can successfully resolve the Apache 500 error and ensure the smooth operation of the WordPress website. Happy debugging!