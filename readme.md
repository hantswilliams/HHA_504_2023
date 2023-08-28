# HHA-504-2023 Class Repository

## 1. **Introduction to 504 Class**
### Lecture Topic:
- Syllabus Review
- Hospital Priceline Overview
- Introduction to Google Cloud Platform (GCP) and Microsoft Azure
- Main Principles of Cloud Computing: Storage, Compute, and Database services

### Subtopics:
- Overview of GCP and Azure platforms
- Introduction to cloud-based Storage, Compute, and Database concepts
- Key differences and similarities between GCP and Azure
- Introduction to GCP and Azure Python SDKs

### Azure/GCP Resources:
- [Azure for Python](https://learn.microsoft.com/en-us/azure/developer/python/)
- [GCP for Python](https://cloud.google.com/python)

### Homework:
- Register for free student account (with your .edu) on Microsoft Azure 
- You will be receiving GCP access codes from me
- Explore the Azure dashboard and list out 5 services under each of the main principles: 
    - Storage
    - Compute
    - Database services. 


---

## 2. **Application Structure and Basics**
### Lecture Topic:
- Introduction to Flask and FastAPI as Python web frameworks

### Subtopics:
- Basic project structure
- Understanding Routes and Views
- Introduction to Jinja templating
- Deploying a Python web application on Azure App Service
  - Understanding the Azure App Service Environment
  - Configuring a web application for deployment on Azure
  - Deploying the application and accessing it via the provided URL

### Azure/GCP Resources:
- [Azure App Service Quickstart for Python](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python)

### Homework:
1. Set up a basic Flask application and create a home page using Jinja templating.
2. Deploy your Flask application to Azure App Service using the resources provided in the lecture. Provide the deployed URL in your submission.
3. (Optional) Explore FastAPI and try deploying a basic FastAPI application on Azure App Service.

---

## 3. **Datasets and Databases**
### Lecture Topic:
- Introduction to Hospital pricing transparency data
- Introduction to SQLite
- SQLalchemy: Bridging Python and Databases
- Introduction to pandas' `to_sql` function

### Subtopics:
- Data exploration: what information is available and its relevance
- Data preprocessing: cleaning and formatting the data
- Introduction to SQLalchemy:
  - ORM (Object Relational Mapping) basics
  - Model definition and database connections
  - Setting up SQLite with Flask using SQLAlchemy
- Using pandas for database operations:
  - Introduction to `to_sql` function
  - Reading and writing data between DataFrame and SQL database
- Basic CRUD operations
- Transitioning to cloud-based databases

### Azure/GCP Resources:
- [Google SQL Server](https://cloud.google.com/sql/docs/sqlserver/connect-overview#python)
- [Google Cloud BigQuery](https://cloud.google.com/python/docs/reference/bigquery/latest)
- [Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/connect-query-python)

### Homework:
1. Import at least two different hospital system pricing transparency datasets into a pandas DataFrame. Conduct a basic exploratory analysis using Python.
2. Set up a local SQLite database and use the `to_sql` function from pandas to push tables from the DataFrame to this database.
3. Push the cleaned and preprocessed data to databases in both Azure SQL Database and Google SQL Server. Provide the connection string (without credentials) or database URL for verification.
4. (Optional) Write custom SQL queries to perform a basic analysis on the data pushed to Azure and GCP databases.

---

## 4. **Diving Deeper into Databases**
### Lecture Topic:
- Setting up MySQL on a Virtual Machine
- Connection Pooling: Importance and Management
- Migrations: Evolving Your Database with Your Application

### Subtopics:
#### MySQL on a VM:
- The basics of virtualization and its importance in the cloud.
- Installing MySQL on a VM: step-by-step walkthrough.
- Understanding MySQL configurations, tuning, and security considerations.

#### Connection Pooling:
- What is a connection pool and why is it important?
- Max connections, waiting times, and other crucial parameters.
- Pooling implications for web apps, especially in serverless/static site environments like Vercel.
- Potential issues and their impact: connection leaks, timeouts, etc.

#### Database Migrations with Python:
- What are migrations and why do we need them?
- Introduction to popular migration tools/frameworks in Python like Alembic.
- Writing, applying, and rolling back migrations.
- Integrating migrations into a CI/CD pipeline.

### Resources:
- [Alembic](https://github.com/sqlalchemy/alembic)
- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)
- [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

### Homework:
1. Install MySQL on a VM provided by Azure or GCP. Secure your installation and create a simple database with a couple of tables.
2. For the Flask application from earlier assignments, implement connection pooling. Monitor and document how the app behaves under various connection scenarios (e.g., simulate high traffic).
3. Introduce a significant change in your application (like adding a new feature) that requires database changes. Implement a migration to handle this change. Document the steps and results.

---

## 5. **Frontend and Styling**
### Lecture Topic:
- Introduction to HTML, CSS, and Tailwind
- Introduction to Content Delivery Networks (CDN) and its importance

### Subtopics:
- Using Tailwind with Flask: How to integrate and serve static assets
- Understanding CDNs: Principles and benefits
- Setting up and using Google Cloud CDN for hosting and delivering static assets
- Creating forms for user input using Tailwind
- Displaying search results with styled components
- Best practices for organizing static assets in a web application

### Azure/GCP Resources:
- [Tailwind](https://v2.tailwindcss.com/docs)
- [Google Cloud CDN](https://cloud.google.com/cdn)
- [Google Cloud CDN with Flask](https://cloud.google.com/appengine/docs/flexible/serving-static-files?tab=python)

### Homework:
1. Design a search page using Tailwind CSS for the Hospital Priceline application. The design should be responsive and adhere to good user experience principles.
2. Incorporate at least two static images relevant to the Hospital Priceline theme into your design (e.g., a hospital or medical symbol, a price tag icon, etc.).
3. Host the Tailwind CSS library, the static images, and any other relevant assets on Google Cloud CDN. Use these CDN-hosted assets in your Flask application.
4. Optimize your page load by ensuring that the static assets are being served from the CDN. Provide screenshots or other proof that the assets are being delivered from the CDN.
5. (Optional) Explore Google Cloud CDN's caching rules and apply a custom caching rule for one of your assets. Document the configuration and its expected behavior.

---

## 6. **API Endpoints with Flask and FastAPI**
### Lecture Topic:
- Designing RESTful APIs using Flask and FastAPI
- Introduction to OpenAPI Specification

### Subtopics:
- The architecture of RESTful APIs: resources, methods, and status codes
- Creating endpoints for data retrieval in Flask using extensions like Flask-RESTful
- Introduction to FastAPI:
  - Why FastAPI? Speed, automatic validation, and automatic OpenAPI Specification
  - Setting up and designing simple endpoints with FastAPI
  - Automatic generation of the OpenAPI specification using FastAPI
- Understanding the OpenAPI Specification:
  - Its purpose and benefits
  - OpenAPI's role in Azure API Management
  - Exploring generated OpenAPI spec from FastAPI
- API security considerations: 
  - Rate limiting, API keys, JWT tokens, OAuth2

### Python Packages:
- Flask-RESTful: For creating RESTful APIs in Flask
- FastAPI: For creating RESTful APIs with automatic OpenAPI Specification
- Pydantic: For data validation and serialization in FastAPI
- Uvicorn: ASGI server to run FastAPI applications

### Resources:
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [Fast API](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [Azure API Management](https://azure.microsoft.com/en-us/services/api-management/)
- [Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/)
- [Azure API Management Tutorial](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish)

### Homework:
1. Develop a RESTful endpoint in Flask to search for pricing data by CPT code. Use Flask-RESTful to facilitate this.
2. Replicate the same endpoint using FastAPI. Observe the differences in setup, design, and performance.
3. Extract the automatically generated OpenAPI Specification from the FastAPI app.
4. Integrate your FastAPI app with Azure API Management using the OpenAPI spec.
5. (Optional) Implement a basic form of API security (API key, JWT token) for both Flask and FastAPI endpoints using Azure API management.

---

## 7. **User Authentication and Management**
### Lecture Topic:
- User registration, authentication, and identity management in web applications

### Subtopics:
- Basics of user authentication:
  - Importance of secure authentication
  - Password hashing and storage best practices
- Session management in Flask using Flask-Session
  - Understanding sessions: persistent vs. non-persistent
  - Handling user sessions using `flask_session`
- Introduction to `identity` and `identity.web` for Flask
  - Setup and configuration
  - Handling authentication flow with these modules
- Transitioning to cloud-based authentication:
  - Advantages of managed identity platforms
  - Introduction to Azure Active Directory B2C and Google Cloud Identity Platform
  - Integration with Flask: creating sign-in and sign-out functionality

### Azure/GCP Resources:
- [Azure Active Directory B2C](https://azure.microsoft.com/en-us/services/active-directory-b2c/)
- [Google Cloud Identity Platform](https://cloud.google.com/identity-platform)
- [Azure Managed Identity with Python](https://learn.microsoft.com/en-us/azure/active-directory/develop/scenario-web-app-sign-user-overview?tabs=python)

### Python Packages:
- Flask-Session: For managing sessions in Flask applications
- Identity: To handle authentication and identity in Flask
- Requests: For making HTTP requests

### Homework:
1. Set up Flask-Session in your Hospital Priceline application to manage user sessions.
2. Utilizing the `identity` and `identity.web` modules, implement a user authentication system for Hospital Priceline. This should include:
   - User registration with password hashing
   - User login with session creation
   - User logout with session destruction
3. Integrate a cloud-based authentication system, either Azure Active Directory B2C or Google Cloud Identity Platform, into your application. Add sign-in and sign-out buttons to the app's UI. 
4. Follow the [Azure Managed Identity with Python](https://learn.microsoft.com/en-us/azure/active-directory/develop/scenario-web-app-sign-user-overview?tabs=python) tutorial to further enhance and secure your authentication flow.

---

## 8. **Deployment**
### Lecture Topic:
- Deployment strategies and platforms for Flask and FastAPI applications

### Subtopics:
- Introduction to Vercel:
  - Benefits of static site deployment services
  - Deploying Flask/FastAPI apps as serverless functions on Vercel
- Understanding CI/CD (Continuous Integration/Continuous Deployment):
  - The importance of CI/CD in modern web development
  - Setting up automated deployment pipelines with GitHub Actions
- Deploying to Google Cloud Run and Azure App Service:
  - Basic setup and deployment steps
  - Scaling and monitoring deployed apps
- Advanced: Introduction to containerization with Docker:
  - Basics of Docker and Docker Hub
  - Containerizing a Flask/FastAPI application
  - (Optional) Deploying containerized apps using Azure Container Apps

### Azure/GCP Resources:
- [Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python)
- [Google Cloud Run](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service)
- [Azure Container Apps](https://learn.microsoft.com/en-us/azure/developer/python/tutorial-containerize-simple-web-app)
- [Vercel Deployment for Python Flask](https://github.com/vercel/examples/tree/main/python/flask)
- [GitHub Actions for Python](https://docs.github.com/en/actions/guides/building-and-testing-python)
- [GitHub Actions for Python with Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/deploy-github-actions?tabs=applevel)


### Homework:
1. Deploy your Hospital Priceline application to Vercel and set up a custom domain for your service (optional).
2. Deploy the same application to both Google Cloud Run and Azure App Service.
3. Set up a basic CI/CD pipeline using GitHub Actions to automate deployment whenever you push to a specific branch in your GitHub repository for the Azure App Service.
4. (Optional) Containerize your Flask/FastAPI application using Docker, push it to Docker Hub, and then deploy the containerized app to Azure Container Apps.

---

## 9. **Logging, Monitoring, and Debugging**
### Lecture Topic:
- Importance and methodologies of logging, monitoring, and debugging in Python applications.

### Subtopics:
- Fundamentals of logging in Python:
  - Introduction to Python's built-in [`logging`](https://docs.python.org/3/library/logging.html) module.
  - Understanding different logging levels (INFO, DEBUG, ERROR, etc.)
  - Configuring log outputs and formats.
- Third-party logging tools and extensions:
  - [Loguru](https://github.com/Delgan/loguru): Simplified file logging and pretty console logs.
  - [Sentry](https://sentry.io): Real-time error tracking and monitoring.
  - [Graylog](https://www.graylog.org) & [ELK Stack](https://www.elastic.co/what-is/elk-stack): Log aggregation and visualization.
  - [structlog](https://www.structlog.org/en/stable/): Structured logging.
- Tracing and Debugging:
  - Importance of tracing in distributed applications.
  - Using Python debugging tools.
  - Strategies for debugging deployed applications.
- Performance Monitoring:
  - Identifying and monitoring critical performance metrics.
  - Setting up alerts and notifications.
- Transition to cloud-based logging, monitoring, and advanced tracing:
  - Introduction to distributed tracing.
  - Integrating Flask with cloud logging services.
  - Advanced tools and platforms for monitoring application health and performance.

### Resources:
- [Azure Monitor and Log Analytics](https://azure.microsoft.com/en-us/services/monitor/)
- [Google Cloud Monitoring and Logging](https://cloud.google.com/products/operations)
- [OpenCensus] (https://opencensus.io)
- [Azure Monitor with Opencensus-Python](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opencensus-python)

### Homework:
1. Integrate Python's built-in logging module into your Flask application. Ensure logs are written at different severity levels (INFO, WARNING, ERROR).
2. Set up distributed tracing for your application using OpenCensus or a similar platform.
3. Integrate your application with Azure Monitor or Google Cloud Monitoring, and set up basic performance metrics monitoring.
4. Trigger an error within your application intentionally and utilize your logging setup to diagnose the issue.
5. (Optional) Set up alerts or notifications based on specific conditions (e.g., server response time exceeding a threshold) in Azure Monitor or Google Cloud Monitoring.
---

## 10. **Scaling and Performance**
### Lecture Topic:
- Scaling Flask applications

### Subtopics:
- Basics of Scaling:
  - Differences between horizontal and vertical scaling.
  - Stateless vs. Stateful applications: Why being stateless aids scaling.
- Load Balancers:
  - The role of load balancers in scaling.
  - Different types of load balancing: Application layer vs. Network layer.
  - Sticky sessions and why they matter.
  - Health checks and the importance of monitoring with load balancers.
- Databases and Scaling:
  - Challenges in scaling databases.
  - Introduction to sharding and replication.
  - Database caching mechanisms.
- Application Performance:
  - Understanding performance bottlenecks in Flask applications.
  - Profiling and monitoring tools for Flask.
  - Optimizing Flask app configurations for better performance.
- Cache Mechanisms:
  - Caching strategies for web applications.
  - Introduction to tools like Redis and Memcached.
  - Cache eviction policies and potential issues.
- Auto-scaling:
  - The importance of metrics in auto-scaling.
  - Implementing auto-scaling in cloud environments.
  - Pros and cons of auto-scaling.
- Microservices and Scaling:
  - Breaking monolithic applications into microservices for better scalability.
  - Introduction to service orchestration and containerization.

### Python Tools to Simulate Traffic:
#### 1. **Locust.io**
- **About**: Locust is an open-source load testing tool written in Python. It lets users define behavior using Python code and simulate millions of simultaneous users to load-test web applications.
- **Website**: [Locust.io](https://locust.io/)
#### 2. **Flask-Testing for Flask**
- **About**: Flask-Testing provides testing utilities specific to Flask. It can be used in combination with `pytest` for a seamless testing experience with Flask apps.
- **Website**: [Flask-Testing on PyPi](https://pypi.org/project/Flask-Testing/)

### Azure/GCP Resources:
- [Azure Load Balancer](https://azure.microsoft.com/en-us/services/load-balancer/)
- [Google Cloud Load Balancing](https://cloud.google.com/load-balancing)

### Homework:
1. Set up a basic load balancer for your Flask application on either Azure or Google Cloud. Ensure it routes traffic to multiple instances of your application.
2. Integrate a caching solution (e.g., Redis) into your Flask application to cache frequent database queries or static assets.
3. Simulate high traffic using tools like locust.io. Monitor how your application handles the load and identify potential bottlenecks.
4. Implement basic auto-scaling rules based on CPU or memory usage for your Flask application.
5. Research a high-traffic web application (like Twitter, Netflix, or any other of your choice). Write a 1 page report on how it handles scaling, the strategies it employs, and potential challenges it faces. Dive deep into aspects like CDN usage, database scaling techniques, and how they handle peak loads (like during a major event).
6. (Optional) Look into containerizing your Flask application with Docker, then deploy it on a platform like Azure Kubernetes Service or Google Kubernetes Engine. Discuss the benefits this might bring to scaling.

---

## 11. **Storage**
### Lecture Topic:
- File storage in Flask applications

### Subtopics:
- Differences between blob/general storage and databases
- Considerations for when to use general storage vs. databases
- Pros and cons of local vs. cloud storage
- Addressing the cost-effectiveness of cloud storage solutions
- File upload and retrieval mechanisms in Flask

### Azure/GCP Resources:
- [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/)
- [Google Cloud Storage](https://cloud.google.com/storage)

### Homework:
1. Modify Hospital Priceline to allow users to upload proof of pricing (e.g., a bill). Initially, store this file locally in the Flask app.
2. Transition your local storage solution to either Azure Blob Storage or Google Cloud Storage. Adjust your app to read and write the uploaded files from/to this cloud storage.
3. Research and write a brief report on the pricing model of your chosen cloud storage solution and how it compares to traditional hosting or databases in terms of cost.


---

## 12. **Security Best Practices**
### Lecture Topic:
- Securing Flask applications

### Subtopics:
- Importance of `.env` files for secure token and key management
- Deployment strategies: Protecting sensitive keys and tokens during deployment
- Data encryption strategies: at-rest and in-transit
- Services for testing security: 
  - Subdomain enumeration countermeasures
  - Mitigating ransomware threats
  - Protecting against password attacks
- Leveraging cloud security: Automatic features and tools provided by cloud providers
- Understanding the 'Shared Responsibility' model in cloud security

### Azure/GCP Resources:
- [Azure Security Center](https://azure.microsoft.com/en-us/services/security-center/)
- [Google Cloud Security Command Center](https://cloud.google.com/security-command-center)

### Homework:
1. Implement `.env` files in Hospital Priceline, ensuring that sensitive information is not exposed.
2. Use Azure Security Center or Google Cloud Security Command Center to run a security assessment on your Hospital Priceline deployment. Document any findings and proposed solutions.
3. Research and write a brief essay on the 'Shared Responsibility' model. Explain its significance and how it impacts developers and businesses using cloud platforms.
4. Identify 3 potential security vulnerabilities in Hospital Priceline, and for each, provide a proposed solution and implementation strategy to mitigate the risk. You do not need to write any code for this. 

---

## 13. **Serverless and Event-Driven Architectures**
### Lecture Topic:
- Introduction to serverless architectures and event-driven computing

### Example Subtopics:
- What are serverless architectures? Understanding FaaS (Function as a Service)
- Creating cloud functions in Python for data processing
- Integrating serverless functions into existing applications
- Triggers and bindings in serverless platforms
- Benefits of serverless: Cost-efficiency, scalability, and reduced management overhead
- Drawbacks of serverless: Cold starts, state management, and potential for vendor lock-in

### Azure/GCP Resources:
- [Azure Functions](https://azure.microsoft.com/en-us/services/functions/)
- [Azure Functions Python Developer Guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
- [Google Cloud Functions](https://cloud.google.com/functions)
- [Google Cloud Functions Tutorial for Python](https://cloud.google.com/functions/docs/tutorials/http)

### Homework:
1. Develop a serverless function that performs an analytical task on the hospital pricing data, such as calculating the average price for a certain procedure across all hospitals. This offloads the analytical processing, keeping the main application snappy.
2. Create another function to send email notifications to users when new hospital pricing data is available or when there are significant changes in pricing.
3. Integrate these serverless functions into the Hospital Priceline application, ensuring that they are triggered appropriately (e.g., upon data update).
4. Document the performance and latency benefits observed from offloading the analytical processing to a serverless function.

---

## 14. **Final Project / Capstone**
### Lecture Topic:
- Design and implementation of a cloud-based project
- Ideation and brainstorming: How to think of new features that enhance user experience

### Example Subtopics:
- Visualizing data in a meaningful way for users (e.g., bar charts, pie charts, heat maps)
- Introduction to simple ML/AI integrations (e.g., predicting average hospital costs based on historical data)
- Incorporating social media integrations for sharing content
- Using third-party Python libraries to quickly implement new features
- Importance of user feedback in shaping features

### Suggested Features:
1. **Data Visualization**: Use libraries like `matplotlib`, `bokeh`, or `plotly` to create visual representations of hospital pricing data.
2. **ML/AI Integration**: Use `scikit-learn` or `tensorflow` to predict future pricing or identify anomalies in the data.
3. **Social Media Sharing**: Integrate buttons using `Flask-Dance` or other Flask extensions to enable sharing of specific pricing insights on platforms like Facebook, Twitter, or LinkedIn.
4. **Feedback System**: Implement a user feedback or rating system to understand the most useful features or data points.
5. **Notifications**: Use third-party services like `Twilio` for SMS notifications or `SendGrid` for email notifications to alert users about significant changes in pricing.

### Homework:
1. Design and implement at least two new features for the Hospital Priceline application, based on the suggested features or your own ideas.
2. Ensure that the new features align well with the cloud resources learned throughout the course.
3. Present the developed project, showcasing its enhanced functionality, scalability, the cloud services utilized, and a brief explanation of the chosen features' relevance and importance.


---

## 15. **Course Recap and Future Trends**
### Lecture Topic:
- Reflection on the course

### Example Subtopics:
- Future trends in cloud and health informatics
- Further study and resources

### Homework:
- Final Project continuation

---
