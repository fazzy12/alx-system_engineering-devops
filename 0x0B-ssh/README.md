# SSH Project

![SSH Logo](zPVRKhPsUP5lK.gif)

## Overview

This project is part of the Software Engineering course, specifically in the area of DevOps, Network, SysAdmin, and Security. The focus of the project is to explore and implement SSH (Secure Shell) for secure remote access to an Ubuntu server.

**Author:**  [Ifeanyi Kalu](www.github.com/fazzy12)



## Curriculum

**Topics Covered:**
- DevOps
- SSH
- Network
- SysAdmin
- Security

**Instructor:** Sylvain Kalache

### Learning Objectives

Upon completion of this project, you are expected to:

- Explain the concept of a server and its typical location.
- Understand what SSH is and its importance in secure remote access.
- Create an SSH RSA key pair.
- Connect to a remote host using an SSH RSA key pair.
- Appreciate the advantages of using `#!/usr/bin/env bash` over `/bin/bash`.

## Requirements

**General:**
- Allowed editors: vi, vim, emacs
- Interpret on Ubuntu 20.04 LTS
- All files should end with a new line
- A README.md file at the root of the project folder is mandatory
- All Bash script files must be executable
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining the script's purpose

**Servers:**
- The provided servers include:
  - Name: 57446-web-01, Username: ubuntu, IP: 18.207.112.235, State: running

## Tasks

### 0. Use a private key

```bash
./0-use_a_private_key
```
Write a Bash script that uses SSH to connect to the server using the private key ~/.ssh/school with the user ubuntu.

Requirements:

- Use only SSH single-character flags.
- Do not use -l.
- No need to handle the case of a private key protected by a passphrase.

1. Create an SSH key pair

```
./1-create_ssh_key_pair
```
Write a Bash script that creates an RSA key pair.

Requirements:

- Name of the created private key: school
- Number of bits in the created key: 4096
- The created key must be protected by the passphrase betty

2. Client configuration file

Edit your machine's SSH configuration file for the local SSH client to  connect to a server without typing a password.

Requirements:

- Configuration to use the private key ~/.ssh/school.
- Configuration to refuse authentication using a password.

3. Let me in!
Now that you've successfully connected to your server, add the provided SSH public key to your server to allow connection using the `ubuntu` user.

4. Client configuration file (w/ Puppet)

sudo puppet apply `100-puppet_ssh_config.pp`
Use Puppet to set up your client SSH configuration file to connect to a server without typing a password.

Requirements:

- Configuration to use the private `key ~/.ssh/school`.
- Configuration to refuse authentication using a password.

Copyright © 2023 ALX, All rights reserved.
