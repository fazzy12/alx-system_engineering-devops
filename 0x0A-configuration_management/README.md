<div style="width: 100%; height: 0; padding-bottom: 50%; position: relative;">
    <img src="4i8il3B.gif" alt="OOP Image" style="position: absolute; width: 800%; height: 100%; object-fit: cover;">
</div>


# Configuration Management Project

## Overview

This configuration management project is part of the SE Foundations curriculum and focuses on Puppet, a widely used configuration management tool. The project includes tasks that cover creating files, installing packages, and executing commands using Puppet.

## Background Context

The inspiration for this project comes from real-world experiences, such as the incident at SlideShare where an auto-remediation tool, Skynet, played a crucial role in restoring the infrastructure after a critical bug. The incident highlights the importance of automated configuration management, specifically using tools like Puppet.

## Curriculum Information

- **Average Score:** 122.47%
- **Project Duration:** Dec 9, 2022, 6:00 AM - Dec 10, 2022, 6:00 AM
- **Auto QA Review:** 7.0/9 mandatory (77.78%)

## Resources

- [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
- [Puppet resource type: file](https://www.puppet.com/docs/puppet/5.5/types/file.html)
- [Puppet’s Declarative Language: Modeling Instead of Scripting](https://www.puppet.com/blog)
- [Puppet lint](http://puppet-lint.com/)
- [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)
- [Puppet vim mode](https://github.com/rodjek/vim-puppet)
- [step by step Youtube video by Sylvain](https://www.youtube.com/watch?v=xmzbbe5bxrQ)

## Requirements

- All files interpreted on Ubuntu 20.04 LTS
- All files end with a new line
- Mandatory README.md file at the root of the project folder
- Puppet manifests must pass puppet-lint version 2.1.1 without errors
- Puppet manifests must run without errors
- Puppet manifests must have a comment explaining their purpose as the first line
- Puppet manifest files must end with the extension .pp

### Note on Versioning

- Ubuntu 20.04 VM should have Puppet 5.5 preinstalled
- Puppet installation commands provided

## Tasks

### 0. Create a File

- Using Puppet, a file named "school" is created in /tmp with specified permissions, owner, group, and content.

### 1. Install a Package

- Using Puppet, Flask version 2.1.0 is installed from pip3.

### 2. Execute a Command

- Puppet manifest is created to kill a process named "killmenow" using the exec resource and pkill.

## Getting Started

To get started, follow the instructions in the README.md file. Make sure to have the necessary prerequisites installed, including Puppet 5.5.

## Contributing

Contributions to this project are welcome. Please follow the guidelines outlined in the project's README.md file.

**Copyright © 2023 ALX, All rights reserved.**

