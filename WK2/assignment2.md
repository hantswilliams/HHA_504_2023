## **Week 2 Homework Assignment: Introducing Flask and Azure Deployment**

### **Objective**:
Get hands-on experience setting up a Flask application, integrate it with data processing via Pandas, and deploy the app on Azure App Service. You'll also practice documenting your process and using GitHub for project management.

### **Instructions**:

#### **1. Setting Up Your Flask Application**:
- Initiate a new Flask application. You can use one of my to start. I would recommend WK2 -> `flaskapp_0`, or if you want to go off of the more advanced modular version, please see `flaskapp_1`  
- Integrate Jinja templating to set up a homepage (`base.html`) for your app. 
- **OPTIONAL**: Use Pandas to load data from a provided file (choose a format: CSV, JSON). Ensure that your data file is less than 10MB for efficient loading. 
  - Display the data on your homepage using a basic table.
  - The code that you will want to modify is found in the `app.py` file and in the `data.html` files 

#### **2. Deploying on Azure App Service**:
- Deploy your Flask application to Azure App Service.
  - Use the lecture resources as a guide.
  - For additional help, refer to the [Azure App Service Quickstart for Python](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python).
- Make sure your application is live and accessible via the provided URL. 

#### **(Optional) FastAPI Exploration**:
- Explore the FastAPI framework.
- Set up and deploy a basic FastAPI application on Azure App Service.

#### **3. Preparing Your GitHub Submission**:
- Create a new GitHub repository named `azure_flask_deployment` in your GitHub account.
- Feel free to re-use parts of your code from prior assignments where necessary 
  - Include your Python code for the Flask application.
  - Upload the data file you used.
  - Ensure your README.md file clearly details:
    - A step-by-step guide on how you set up and deployed your application. Imagine you're guiding someone unfamiliar with the process.
    - Make use of markdown features, especially code blocks, to format your instructions neatly. For reference on markdown syntax, refer to the [Markdown Guide](https://www.markdownguide.org/basic-syntax/).
  - Provide the deployed URL of your application in this README.

### **Submission**:
- Share the link to your `azure_flask_deployment` GitHub repository as your assignment submission.
- Ensure your repository is public so that it's accessible for review.

**Tip**: Keep your commits regular and meaningful. This not only backs up your work but also provides a trail of your progress and understanding.

