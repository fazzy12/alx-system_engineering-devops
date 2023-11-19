# Web Server Configuration Project

  <div style="flex: 1; padding: 10px;">
    <img src="img2.png" alt="Header Image 2" style="max-width: 100%; height: 500px;">
  </div>


## Overview

This project focuses on configuring a web server, specifically Nginx, on an Ubuntu machine. The tasks involve transferring files, installing Nginx, setting up a domain name, configuring redirection, and implementing a custom 404 page. Additionally, there's an advanced task to install and configure Nginx using Puppet.

## Concepts

Throughout the project, you will explore and understand the following concepts:

- **Child Process:** Learn about the role of child processes in the context of web servers.

## Automation and Scripting

Tasks emphasize automating configurations, encouraging the creation of Bash scripts to perform tasks without manual intervention. Automation is crucial for efficient server management, especially in scenarios with numerous servers.

## Learning Objectives

By the end of this project, you should be able to:

- Explain the main role of a web server.
- Understand the concept of a child process and why web servers use parent and child processes.
- Identify and describe main HTTP requests.
- Define DNS, its main role, and various DNS record types (A, CNAME, TXT, MX).

<div style="flex: 1; padding: 10px;">
  <img src="img.jpg" alt="Header Image 1" style="max-width: 100%; height: 500px;">
</div>

## Project Structure

The project is organized into several tasks, each targeting specific aspects of web server configuration. Here's an overview of the main tasks:

1. **Transfer a file to your server:** Write a Bash script that transfers a file to a server using SCP.

2. **Install Nginx web server:** Install and configure Nginx on your server, ensuring it listens on port 80 and returns a "Hello World!" page.

3. **Setup a domain name:** Obtain a free domain name, configure DNS records, and point the root domain to your web server's IP address.

4. **Redirection:** Configure Nginx to redirect requests from `/redirect_me` to another page using a "301 Moved Permanently" response.

5. **Not found page 404:** Create a custom 404 page on Nginx containing the string "Ceci n'est pas une page."

6. **Install Nginx web server (w/ Puppet):** Use Puppet to install and configure Nginx, including a 301 redirect for `/redirect_me`.

## Usage and Testing

Detailed examples and usage instructions are provided for each task. It's recommended to test scripts and configurations in a controlled environment, reproducing the checker's setup.

## Resources

The README includes references to relevant resources, such as documentation on how the web works, Nginx configuration, DNS concepts, and more. These resources can be consulted for further understanding.

## Important Notes

- All files must end with a new line.
- A README.md file is mandatory at the root of the project folder.
- Bash scripts must pass Shellcheck without any errors.
- Avoid using systemctl for restarting a process.

## Conclusion

This project aims to reinforce your understanding of web server configuration, automation, and scripting. Following the provided instructions and examples will help you successfully complete each task and achieve the learning objectives.

© 2023 ALX. All rights reserved.
