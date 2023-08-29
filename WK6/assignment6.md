## **Week 6 Homework Assignment: Building and Managing APIs with Flask, FastAPI, and Azure**

### **Objective**:
The goal of this week's assignment is to develop, document, and manage APIs using Flask and FastAPI. You'll also explore the differences between the two frameworks and integrate your APIs with Azure API Management.

### **Instructions**:

#### **1. Flask-based RESTful API**:
- Utilize Flask-RESTful to develop an endpoint in Flask that enables users to search for pricing data based on the CPT code.
- Document your API endpoint: specify the expected request format, method (GET, POST, etc.), any required headers, and the expected response format.

#### **2. Replicating with FastAPI**:
- Reproduce the same endpoint functionality using FastAPI.
  - Document any differences you notice in terms of setup, coding, and performance between Flask and FastAPI.
  - Take note of FastAPI's built-in tools and automatic validations, and how they compare with Flask.

#### **3. OpenAPI Specification and Documentation**:
- Extract the OpenAPI Specification that FastAPI automatically generates for your app.
- Use this specification to understand and document your API in a standard format. Discuss its advantages and why such specifications are essential in modern API development.

#### **4. Azure API Management Integration**:
- Integrate your FastAPI application with Azure API Management using the extracted OpenAPI specification.
  - Document the steps taken to achieve this integration and the benefits of using Azure API Management for your APIs.

#### **5. API Security with Azure** *(Optional)*:
- Implement basic API security for both your Flask and FastAPI endpoints using Azure API Management.
  - Options to explore: API keys, JWT tokens, etc.
  - Discuss the importance of securing APIs and the benefits of Azure's API management features in this context.

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
