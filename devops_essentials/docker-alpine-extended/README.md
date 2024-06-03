1. Customize Your Alpine-based Docker Image
mandatory
Background:
Building on the foundation of the previous exercise, we’re now diving deeper into creating customized Docker images. By extending a Docker image, you can include additional tools and files, tailoring the container environment to your specific needs.

Objective:
Extend the Docker image created in the previous task to:

Install the curl package.
Add a configuration file named config.txt containing the text “Welcome to Docker!”.
When the Docker container is run, it should be able to execute curl commands. Additionally, the config.txt file should be accessible and contain the specified text.

Instructions:
Setup:

Navigate to the directory of the previous task or create a new directory: mkdir docker-alpine-extended && cd docker-alpine-extended
Configuration File:

In the project directory, create a file named config.txt.
Add the text “Welcome to Docker!” to config.txt.
Dockerfile:

Modify or create a new Dockerfile.
Start with the same Alpine base image as the previous exercise.
Use the RUN directive to install the curl package. For Alpine, this would typically involve apk add --no-cache curl.
Use the COPY directive to add the config.txt file to a suitable location in the container, e.g., /app/config.txt.
Building the Docker Image:

Build the Docker image with the docker build command, and tag it appropriately:
 docker build -t extended-hello-alpine .
Testing the Docker Container:

Run a container from the newly created image.
Test the curl command by fetching a webpage, e.g., docker run extended-hello-alpine curl https://www.google.com.
Confirm the existence and content of the config.txt file, e.g., using docker run extended-hello-alpine cat /app/config.txt.
Notes:

Be cautious about the order of directives in the Dockerfile. The COPY command should come after the installation of necessary packages to make efficient use of Docker’s layer caching.
