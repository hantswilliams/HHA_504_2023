## **Week 6 Homework Assignment: Building and Managing APIs with Flask and Azure**

### **Objective**:
The goal of this week's assignment is to develop and document APIs using Flask, and manage them with Azure API Management.

### **Instructions**:

#### **1. Flask-based RESTful API**:
- Utilize Flask to develop an endpoint that can handle a simple GET request.
- The response should be in JSON format.

#### **2. OpenAPI Specification and Documentation**:
- Apply this to your app from Part 1 of this assignment 
- Update your Flask app to include Swagger/OpenAPI documentation.
- Your app should use the `flasgger` package. Installation and documentation can be found here: [Flasgger GitHub repository](https://github.com/flasgger/flasgger) 
- Provide docstring documentation style for each endpoint as seen in the Flasgger examples.

#### **3. Azure API deployment**: 
- Now we will create a new endpoint based on the below tutorial. This is separate from steps 1 and steps 2.
- Using Azure Functions, re-write your Flask app to be a serverless function using the python package `import azure.functions as func`.
- Example python tutorial for HTTP function: 
    - [Azure Functions Python HTTP Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=macos%2Cbash%2Cazure-cli&pivots=python-mode-decorators) 
- For deploying, creating service via CLI in GCP shell, refer back to Week 2 slides 25, 26, and 27 for instructions on downloading the CLI and selecting the correct service account.
    - Once you have the CLI installed, you will also need to run `sudo apt-get install azure-functions-core-tools-4` as per the tutorial instructions.



### **Submission**:
- Create a new GitHub repository named `flask_6_api_management` in your GitHub account.
- Organize your GitHub repository with the following:
  - Source code for the Flask application.
  - Screenshots or video recordings showcasing the functionality of your API endpoints.
  - The extracted OpenAPI Specification from your Flask app.
  - A detailed README.md file, with:
    - Step-by-step instructions on setting up and testing the Flask endpoint.
    - Documentation of your API, especially focusing on the standard OpenAPI format.
    - Steps and observations on Azure API Management integration.
    - Any challenges encountered, solutions tried, and your conclusions.
- Share the link to your repository as your assignment submission.
- Ensure your repository is public to facilitate review.