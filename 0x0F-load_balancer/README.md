# Load Balancer Configuration Project

## Overview

This project aims to automate the configuration of a web stack with load balancing using Nginx and HAProxy. The goal is to achieve redundancy for web servers, allowing for better scalability and reliability.

## Project Structure

- **`0x0F-load_balancer`**: The main project directory.
  - **`0-custom_http_response_header`**: Bash script to configure Nginx with a custom HTTP header.
  - **`1-install_load_balancer`**: Bash script to install and configure HAProxy for load balancing.
  - **`2-puppet_custom_http_response_header.pp`**: Puppet manifest to automate Nginx configuration with a custom HTTP header.

## Tasks and Descriptions

### Task 0: Double the Number of Webservers

- Configure Nginx on web-02 identical to web-01.
- Add a custom HTTP header, X-Served-By, to track the answering web server.
- Bash script: `0-custom_http_response_header`.

### Task 1: Install Your Load Balancer

- Install and configure HAProxy on lb-01.
- Distribute traffic to web-01 and web-02 using a round-robin algorithm.
- Bash script: `1-install_load_balancer`.

### Task 2: Add a Custom HTTP Header with Puppet

- Use Puppet to automate the creation of a custom HTTP header in Nginx.
- Puppet manifest: `2-puppet_custom_http_response_header.pp`.

## How to Use

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/alx-system_engineering-devops.git
    cd alx-system_engineering-devops/0x0F-load_balancer
    ```

2. Execute the desired scripts:

    ```bash
    # Example: Run the Bash script for Task 0
    ./0-custom_http_response_header
    ```

    ```bash
    # Example: Run the Bash script for Task 1
    ./1-install_load_balancer
    ```

3. Apply Puppet manifest:

    ```bash
    # Example: Apply Puppet manifest for Task 2
    sudo puppet apply 2-puppet_custom_http_response_header.pp
    ```

## Requirements

- All scripts are designed for Ubuntu 16.04 LTS.
- Use `vi`, `vim`, or `emacs` as editors.
- Ensure the first line of Bash scripts is `#!/usr/bin/env bash`.
- Include a `README.md` file at the root of the project.
- Bash scripts must be executable and pass Shellcheck (version 0.3.7) without errors.

## Resources

- [Introduction to load-balancing and HAProxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HTTP header](https://www.techopedia.com/definition/27178/http-header)
- [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)

## Author

- [Ifeanyi Kalu](https://github.com/fazzy12) - Co-founder at Holberton School

---

**Copyright © 2023 ALX, All rights reserved.**
