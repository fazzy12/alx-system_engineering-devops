# Web Infrastructure Design Project

**Author:** Sylvain Kalache, co-founder at Holberton School
**Project Team:** Ifeanyi Kalu
**Project Duration:** November 10, 2022, 6:00 AM - November 14, 2022, 6:00 AM
**Manual QA Review:** EKENE ODIBE on November 15, 2022, 10:43 PM
**Project Completion:** 200.0% (Mandatory: 100.0%, Optional: 100.0%)

## Table of Contents

- [Introduction](#introduction)
- [Concepts](#concepts)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [Task 0: Simple web stack](#task-0-simple-web-stack)
  - [Task 1: Distributed web infrastructure](#task-1-distributed-web-infrastructure)
  - [Task 2: Secured and monitored web infrastructure](#task-2-secured-and-monitored-web-infrastructure)
  - [Task 3: Scale up (Advanced)](#task-3-scale-up-advanced)
- [Copyright and Plagiarism](#copyright-and-plagiarism)

---

## Introduction

Welcome to the Web Infrastructure Design project, part of the System Engineering Foundations curriculum. In this project, i learnt and applied the principles related to web infrastructure design, including concepts such as DNS, monitoring, web servers, network basics, load balancers, and servers.

## Concepts

Before you start with the project, make sure to review the following concepts:

- [DNS](https://intranet.alxswe.com/concepts/12)
- [Monitoring](https://intranet.alxswe.com/concepts/13)
- [Web Server](https://intranet.alxswe.com/concepts/17)
- [Network Basics](https://intranet.alxswe.com/concepts/33)
- [Load Balancer](https://intranet.alxswe.com/concepts/46)
- [Server](https://intranet.alxswe.com/concepts/67)

Additional resources to consult:

- [What is a database](https://intranet.alxswe.com/rltoken/n3CdS3EA5l5psDDKbEhApA)
- [What's the difference between a web server and an app server?](https://intranet.alxswe.com/rltoken/0as4wDlFqyhLhf0f_gedcw)
- [DNS record types](https://intranet.alxswe.com/rltoken/Pl3UoEfAO7K_jUKRLMmnAQ)
- [Single point of failure](https://intranet.alxswe.com/rltoken/uxpx2YhXs10TFLIDg78chA)
- [How to avoid downtime when deploying new code](https://intranet.alxswe.com/rltoken/4ansLu2gtHnoFrNThqyObA)
- [High availability cluster (active-active/active-passive)](https://intranet.alxswe.com/rltoken/TAJeVYy9U9iLaEDd6XkbRA)
- [What is HTTPS](https://intranet.alxswe.com/rltoken/c0zs2MxrmxFLsCPOizxq6g)
- [What is a firewall](https://intranet.alxswe.com/rltoken/j6idMcUTyNEDj1oYDQFmUw)

## Learning Objectives

By the end of this project, you are expected to achieve the following learning objectives:

- **General**:
  - Ability to create a comprehensive diagram of the web stack.
  - Explain the role of each component within the infrastructure.
  - Understand system redundancy.
  - Familiarity with acronyms like LAMP, SPOF, and QPS.
- **Copyright - Plagiarism**:
  - Develop solutions for the tasks independently to meet learning objectives.
  - Strictly avoid plagiarism, as it is not permitted and can result in removal from the program.

## Requirements

**General**:

- A `README.md` file at the root of the project folder is mandatory.
- For each task, create a whiteboard diagram.
- Manually review each task.
- Upload screenshots to an image hosting service and provide the links in the answer file.
- Whiteboard each task in front of a mentor, staff, or student.

## Tasks

### Task 0: Simple web stack

**Score**: 100.0%

Design a simple web infrastructure consisting of one server that hosts a website reachable via www.foobar.com. The infrastructure should include:

- 1 server
- 1 web server (Nginx)
- 1 application server
- 1 application files (your code base)
- 1 database (MySQL)
- Configure the domain name foobar.com with a www record pointing to the server's IP (e.g., 8.8.8.8).

**Key Points to Explain**:

- The role of each component.
- Issues with this infrastructure, including SPOF, downtime during maintenance, and scalability challenges.

[Task 0 Details and Diagram](./0-simple_web_stack)

### Task 1: Distributed web infrastructure

**Score**: 100.0%

Design a three-server web infrastructure that hosts www.foobar.com. The infrastructure should include:

- 2 servers
- 1 web server (Nginx)
- 1 application server
- 1 load balancer (HAproxy)
- 1 set of application files (your code base)
- 1 database (MySQL)

**Key Points to Explain**:

- Reasons for adding each additional element.
- Distribution algorithm for the load balancer.
- Active-Active vs. Active-Passive setup in the load balancer.
- How a database Primary-Replica (Master-Slave) cluster works.

[Task 1 Details and Diagram](./1-distributed_web_infrastructure)

### Task 2: Secured and monitored web infrastructure

**Score**: 100.0%

Design a three-server web infrastructure for www.foobar.com. Ensure it is secured, serves encrypted traffic, and is monitored. The infrastructure should include:

- 3 firewalls
- 1 SSL certificate to serve www.foobar.com over HTTPS
- 3 monitoring clients (data collector for Sumologic or other monitoring services)

**Key Points to Explain**:

- Reasons for adding additional elements (firewalls, SSL certificate, monitoring clients).
- The role of firewalls, HTTPS, and monitoring.
- How the monitoring tool collects data.
- Steps to monitor web server QPS.

[Task 2 Details and Diagram](./2-secured_and_monitored_web_infrastructure)

### Task 3: Scale Up (Advanced)

**Score**: 100.0%

In this advanced task, you are required to create an infrastructure that includes:

- 1 server
- 1 load balancer (HAproxy) configured as a cluster with another load balancer
- Split components (web server, application server, database) on their own servers.

**Key Points to Explain**:

- The reasons for adding each additional element.
- The configuration of load balancers as a cluster.
- Ensure your explanations are in English.

[Task 3 Details and Diagram](./3-scale_up)

## Copyright and Plagiarism

Copyright © 2023 ALX, All rights reserved.