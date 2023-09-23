<div style="width: 100%; height: 0; padding-bottom: 50%; position: relative;">
    <img src="home.png" alt="OOP Image" style="position: absolute; width: 800%; height: 100%; object-fit: cover;">
</div>


# Networking Basics #1

This project is a continuation of the ALX School curriculum, focusing on further understanding networking fundamentals and protocols. In this project, you will dive deeper into concepts such as localhost, IP addresses, and network interfaces.

## Learning Objectives

By the end of this project, you should be able to:

- Explain the significance of localhost (127.0.0.1) and 0.0.0.0 in networking.
- Understand the purpose of the `/etc/hosts` file.
- Display active network interfaces on your machine.

## Resources

To successfully complete this project, refer to the following resources:

- [What is localhost](https://en.wikipedia.org/wiki/Localhost)
- [What is 0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0)
- [What is the hosts file](https://www.makeuseof.com/tag/modify-manage-hosts-file-linux/)
- [Netcat examples](https://www.thegeekstuff.com/2012/04/nc-command-examples/)
- Man pages or help for the following commands:
  - ifconfig
  - telnet
  - nc (netcat)
  - cut

## Project Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 20.04 LTS
- Ensure all files end with a newline character
- A README.md file at the root of the project folder is mandatory
- Make all Bash script files executable
- Ensure your Bash scripts pass Shellcheck (version 0.7.0 or later) without any errors
- The first line of all your Bash scripts should be `#!/usr/bin/env bash`
- Include a comment as the second line of all your Bash scripts explaining what the script does

## Tasks

### 0. Change your home IP

Write a Bash script that configures an Ubuntu server with the following requirements:

- `localhost` resolves to `127.0.0.2`
- `facebook.com` resolves to `8.8.8.8`

Example:

```bash
$ ping localhost
PING localhost (127.0.0.1) 56(84) bytes of data.
...

$ ping facebook.com
PING facebook.com (157.240.11.35) 56(84) bytes of data.
...

$ sudo ./0-change_your_home_IP
...

$ ping localhost
PING localhost (127.0.0.2) 56(84) bytes of data.
...

$ ping facebook.com
PING facebook.com (8.8.8.8) 56(84) bytes of data.
...
```

Note: Remember to revert localhost to 127.0.0.1 if needed.

1. Show attached IPs
Write a Bash script that displays all active IPv4 IPs on the machine it's executed on.

Example:

```
$ ./1-show_attached_IPs | cat -e
10.0.2.15$
127.0.0.1$
...
```

2. Port listening on localhost (Advanced)
Write a Bash script that listens on port 98 on localhost. This script allows you to establish connections to localhost on port 98.


Terminal 0:
```
$ sudo ./100-port_listening_on_localhost
Save to grepper

```
Terminal 1:

```
$ telnet localhost 98
Trying 127.0.0.2...
Connected to localhost.
Escape character is '^]'.
Hello world
test
```

Terminal 0:

```
$ sudo ./100-port_listening_on_localhost
Hello world
test
```
This script can be used for various debugging and network-related tasks.