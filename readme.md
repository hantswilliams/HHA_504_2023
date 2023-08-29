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
- [Azure for Students](https://azure.microsoft.com/en-us/free/students)
- [GCP for Python](https://cloud.google.com/python)
- [GCP for Students](https://cloud.google.com/edu/students)

### Homework:
- [Assignment 1](WK1/assignment1.md)


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
- [Assignment 2](WK2/assignment2.md)


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
- [Assignment 3](WK3/assignment3.md)


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
- [Assignment 4](WK4/assignment4.md)

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
- [Assignment 5](WK5/assignment5.md)

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
- [Assignment 6](WK6/assignment6.md)

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
- [Assignment 7](WK7/assignment7.md)


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
- [Assignment 8](WK8/assignment8.md)

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
- [Assignment 9](WK9/assignment9.md)
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
- [Assignment 10](WK10/assignment10.md)

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
- [Assignment 11](WK11/assignment11.md)


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
- [Assignment 12](WK12/assignment12.md)

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
- [Assignment 13](WK13/assignment13.md)

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
- [Assignment 14](WK14/assignment14.md)


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
