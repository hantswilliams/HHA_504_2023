## **Week 6 Homework Assignment: Building and Managing APIs with Flask, FastAPI, and Azure**

### **Objective**:
The goal of this week's assignment is to develop, document, and manage APIs using Flask. You'll also explore the differences between the two frameworks and integrate your APIs with Azure API Management.

### **Instructions**:

#### **1. Flask-based RESTful API**:
- Utilize Flask to develop an endpoint in Flask that can create a simple API endpoint for a get or post request
- The response should be in JSON 
- 
#### **2. Azure API deployment**: 
- Using Azure Functions, re-write you Flask app to be a serverless function using their style of code with the python package `import azure.functions as func`
- Example python tutorial for http function: 
    - https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=macos%2Cbash%2Cazure-cli&pivots=python-mode-decorators 
- For deploying, creating service via CLI in GCP shell: be sure to re-follow Wk2 slide instructions for downloading CLI and ensuring the right service account is selected: slides 25, 26, 27 from WK2 
    - once have the CLI installed, will have also need to do `sudo apt-get install azure-functions-core-tools-4` based on tutorial instructions

#### **3. GCP Cloud Functions API deployment**:

- Example python tutorial for http function: https://cloud.google.com/functions/docs/create-deploy-http-python 
- can test run in the shell cloud environment via google
    - code: `functions-framework-python --target hello_http --debug`
    - keep in mind when deploying, by default it is going to look for a `main.py` file 
    - if have changed the file name: `functions-framework-python --target hello_http --source main_v1.py --debug`
- set project // `gcloud config set project PROJECT_ID` 
- code to deploy: 

```
  gcloud functions deploy bp-checker-hants \
    --gen2 \
    --runtime=python311 \
    --region=us-east1 \
    --source=. \
    --entry-point=hello_http \
    --trigger-http \
    --allow-unauthenticated
```

- then run the code 
- may get `ERROR: gcloud crashed (ValueError): Duplicate stage key: ARTIFACT_REGISTRY` - just re-run 

#### **4. OpenAPI Specification and Documentation**:
- Update the app to include Swagger/OpenAPI documentation for the flask app
- Your app should use: `https://github.com/flasgger/flasgger` package 
- Provide docstring documentation style for each endpoint as seen here: `https://github.com/flasgger/flasgger#using-docstrings-as-specification`

### **Submission**:
- Create a new GitHub repository named `flask_6_api_management` in your GitHub account.
- Feel free to re-use parts of your code from prior assignments where necessary 
- Organize your GitHub repository with the following:
  - Source code for both Flask and FastAPI applications.
  - Screenshots or video recordings showcasing the functionality of your API endpoints.
  - The extracted OpenAPI Specification from your FastAPI app.
  - A detailed README.md file, with:
    - Step-by-step instructions on setting up and testing both Flask and FastAPI endpoints.
    - Observations on the differences between Flask and FastAPI.
    - Documentation of your APIs, especially focusing on the standard OpenAPI format.
    - Steps and observations on Azure API Management integration.
    - Any challenges encountered, solutions tried, and your conclusions.
- Share the link to your repository as your assignment submission.
- Ensure your repository is public to facilitate review.

**Tip**: Proper API documentation is crucial. It aids developers in understanding, integrating, and extending your application without much hassle.
