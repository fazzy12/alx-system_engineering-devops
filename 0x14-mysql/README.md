# MySQL Installation Project

This project involves installing MySQL on two servers, web-01 and web-02, and performing some basic configuration tasks. The goal is to set up a MySQL primary-replica infrastructure.

## Tasks

### 0. Install MySQL
- Install MySQL version 5.7.x on both web-01 and web-02 servers.
- Make sure that task #3 of the SSH project is completed for both servers.

### 1. Let us in!
- Create a MySQL user named holberton_user on both web-01 and web-02 with the host name set to localhost and the password projectcorrection280hbtn.
- Ensure that holberton_user has permission to check the primary/replica status of your databases.

### 2. If only you could see what I've seen with your eyes
- Create a database named tyrell_corp on web-01.
- Within the tyrell_corp database, create a table named nexus6 and add at least one entry to it.
- Ensure that holberton_user has SELECT permissions on the table.

### 3. Quite an experience to live in fear, isn't it?
- On web-01, create a new user for the replica server named replica_user with the host name set to %.
- replica_user must have the appropriate permissions to replicate the primary MySQL server.

### 4. Setup a Primary-Replica infrastructure using MySQL
- Configure MySQL replication with web-01 as the primary and web-02 as the replica.
- Provide MySQL primary and replica configurations as answer files.

### 5. MySQL backup
- Write a Bash script that generates a MySQL dump, creates a compressed archive, and follows specific naming conventions.

## How to Run

1. Clone this repository.
2. Run the script `./install_mysql.sh` to perform the MySQL installation and configuration tasks.

## Additional Notes

- Ensure SSH configuration is correct on both servers.
- Verify MySQL service status after installation.

