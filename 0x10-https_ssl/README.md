# Project Title

## Overview

This project focuses on implementing HTTPS and SSL-related configurations using HAProxy, with the goal of securing website traffic and understanding essential concepts in web security.

## Table of Contents

- [SE Foundations](#se-foundations)
- [Project Tasks](#project-tasks)
  - [Task 0: World Wide Web](#task-0-world-wide-web)
  - [Task 1: HAProxy SSL Termination](#task-1-haproxy-ssl-termination)
  - [Task 2: No Loophole in Your Website Traffic](#task-2-no-loophole-in-your-website-traffic)
- [Usage](#usage)
- [Issues](#issues)
- [Contributing](#contributing)
- [License](#license)

## SE Foundations

### Concepts Covered

- HTTPS and SSL
- DNS
- Web stack debugging

### Learning Objectives

At the end of this project, participants are expected to be able to:

- Explain the roles of HTTPS and SSL.
- Understand the purpose of encrypting web traffic.
- Implement SSL termination on HAProxy.
- Configure DNS for subdomains and perform web stack debugging.

## Project Tasks

### Task 0: World Wide Web

#### Requirements

- Configure domain zone for subdomains.
- Write a Bash script to display information about subdomains.

#### Example Usage

```
./0-world_wide_web holberton.online
./0-world_wide_web holberton.online web-02
```

## Task 1: HAProxy SSL Termination

### Requirements

- Configure HAProxy to handle encrypted traffic.
- Create a certificate using certbot.
- Serve encrypted traffic returning the root of the web server.

### Example Usage

```
curl -sI https://www.holberton.online
curl https://www.holberton.online
```

## Task 2: No Loophole in Your Website Traffic

### Requirements

- Enforce HTTPS traffic.
- Configure HAProxy to redirect HTTP traffic to HTTPS.

### Example Usage

```
curl -sIL http://www.holberton.online
```
## Usage

1. Clone the repository:

```bash
git clone https://github.com/your_username/your_project.git
cd your_project
```

2. Follow the instructions in each task directory.

### Issues
If you encounter any issues or have suggestions, please open an `issue`.

### Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

