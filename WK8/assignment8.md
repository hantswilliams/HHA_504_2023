## **Homework Assignment: Dockerizing Flask Applications**

### **Objective**:
This assignment aims to provide hands-on experience in Dockerizing Flask applications, first individually and then using Docker Compose for managing multiple applications.

### **Part One: Dockerizing a Single Flask Application**

#### **1. Setting Up and Dockerizing a Flask App**:
- In a folder named `Part1`, create a simple Flask application.
- Write a Dockerfile to containerize this Flask application.
  - Include comments in the Dockerfile explaining each command.
- Build the Docker image and run the container.
  - Document the build and run commands you used.
  - Ensure the application is accessible locally.

#### **2. Documentation**:
- Document the steps you took to Dockerize the Flask application.
- Highlight any challenges faced and how they were resolved.
- Explain the significance of each step in the Dockerfile.

### **Part Two: Multi-Container Setup with Docker Compose**

#### **1. Preparing Two Flask Applications**:
- In a folder named `Part2`, create two distinct Flask applications.
  - Each application should have a unique feature or functionality.

#### **2. Dockerizing with Docker Compose**:
- Write Dockerfiles for both Flask applications.
- Create a `docker-compose.yml` file to run both applications simultaneously.
  - Explain each section of the `docker-compose.yml` file.
- Use Docker Compose to build and run your multi-container setup.
  - Document the specific commands used to manage the Docker Compose lifecycle.

#### **3. Documentation**:
- Document the process of setting up and running the two Flask applications with Docker Compose.
- Discuss the role of Docker Compose and how it differs from using Docker alone.
- Note any challenges encountered and how they were addressed.

### **Submission**:
- Create a new GitHub repository named `docker_flask_homework`.
- The repository should contain:
  - The `Part1` and `Part2` folders with respective Flask applications and Dockerfiles.
  - `docker-compose.yml` file for Part Two.
  - A comprehensive README.md file, detailing:
    - The process of Dockerizing the applications in both parts.
    - The build and run commands used.
    - Observations, challenges faced, and reflections on the use of Docker and Docker Compose.
- Submit the link to your GitHub repository.
- Make sure the repository is public for ease of review.

**Tips**:
- Be thorough in your documentation. It's essential for understanding your process and troubleshooting.
- Experiment and explore different configurations and settings in your Dockerfiles and Docker Compose file.

