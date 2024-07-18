Background
Docker Compose is a tool for defining and running multi-container Docker applications. For this exercise, students will work with PostgreSQL, a powerful open-source relational database, and pgAdmin, a popular open-source administration and management tool for the PostgreSQL database.

Objective
Define two services in a Docker Compose YAML file:

PostgreSQL: A relational database management system.
pgAdmin: A web-based administration tool for PostgreSQL.
The main goals are:

Set up a private network that both containers will use.
Allow public access only from the pgAdmin container.
Ensure pgAdmin can connect and manage the PostgreSQL database.
Explicitly configure the dependency between services, so the PostgreSQL container always starts before pgAdmin.
