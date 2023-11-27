# HHA 504 2023 

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

## 2. **Healthcare Web Applications: Intro to Structure, Security, and Deployment**
### Lecture Topic:
- Building and deploying secure web applications for healthcare using Flask and FastAPI.

### Subtopics:
- **Basic Healthcare Application Structure**:
  - Setting up a project with patient data considerations.
  - Prioritizing security and privacy in the application design.
  
- **Security by Design in Healthcare Apps**:
  - Principles and importance of implementing security from the initial stages of design.
  - Best practices and pitfalls to avoid.

- **Routes, Views, and Patient Data Handling**:
  - Understanding routes in the context of patient data requests.
  - Designing views to present health information securely.
  - Importance of data validation to ensure patient data integrity.
  
- **Jinja Templating for Healthcare Web Apps**:
  - Utilizing Jinja to safely render patient information.
  - Techniques to avoid potential security pitfalls in templates.
  
- **HIPAA Compliance and Web Applications**:
  - Basics of HIPAA compliance in web apps.
  - Best practices for storing and transmitting patient data.
  
- **Azure and GCP's Commitment to Healthcare Data Security**:
  - An overview of Azure and GCP's adherence to HIPAA, HITRUST, SOC2, and other security standards.
  - Tools and services provided by these platforms to ensure healthcare data security.
  
- **Deploying a Healthcare Web Application on Azure App Service**:
  - Understanding the Azure App Service Environment's health data handling capabilities.
  - Configuring a web application for deployment on Azure with security in mind.
  - Deploying the application and ensuring secure access via HTTPS.
  - Interoperability with other healthcare platforms and services.

### Azure/GCP Resources:
- [Azure App Service Quickstart for Python](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python)
- [Azure for Health Data and Innovation](https://azure.microsoft.com/en-us/industries/healthcare/)
- [Google Cloud Healthcare Compliance](https://cloud.google.com/security/compliance/hipaa)

### Homework:
- [Assignment 2](WK2/assignment2.md)



---

## 3. **Secure Databases in Healthcare: From Local to Cloud**
### Lecture Topic:
- Ensuring safety and compliance while managing healthcare datasets, focusing on Hospital pricing transparency data.
- Transitioning from local storage like SQLite to cloud-based databases in Azure and GCP.

### Subtopics:
- **Hospital Pricing Transparency Data**: 
  - Data exploration: Understanding the available information and its relevance to health informaticists.
  - Data preprocessing: Techniques for cleaning, formatting, and ensuring the data's accuracy and integrity.
  
- **Working with SQLite in a Healthcare Context**:
  - Introducing SQLite: Strengths and weaknesses for healthcare applications.
  - Ensuring local data encryption and security best practices.
  
- **SQLalchemy for Healthcare Apps**:
  - ORM (Object Relational Mapping) basics and its relevance in handling patient data.
  - Model definition, database connections, and data access controls.
  - Setting up SQLite securely with Flask using SQLAlchemy.
  
- **Pandas and Healthcare Database Operations**:
  - Introduction to the `to_sql` function: safely transitioning healthcare data.
  - Reading and writing patient data between DataFrame and SQL database while maintaining data integrity.
  - Basic CRUD operations with healthcare data considerations.
  
- **Transitioning to Cloud-based Databases**: 
  - Emphasis on data safety and compliance (HIPAA, HITRUST, SOC2).
  - Advantages of cloud databases for scalability, backup, and recovery in healthcare.
  - Access controls, encryption, and security considerations while using Azure/GCP.

### Azure/GCP Resources:
- [Google SQL Server](https://cloud.google.com/sql/docs/sqlserver/connect-overview#python)
- [Google Cloud BigQuery](https://cloud.google.com/python/docs/reference/bigquery/latest)
- [Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/connect-query-python)
- [Azure Health Data Services](https://azure.microsoft.com/en-us/services/azure-api-for-fhir/)
- [Google Healthcare Data Protection Toolkit](https://github.com/GoogleCloudPlatform/solution-acceleration-toolkit)

### Homework:
- [Assignment 3](WK3/assignment3.md)



---

## 4. **Health Informatics Databases: Advanced Setup and Management**
### Lecture Topic:
- Securely setting up MySQL on a Virtual Machine for healthcare applications.
- Efficient and safe database connections via Connection Pooling.
- Ensuring smooth and compliant data transitions using Migrations.

### Subtopics:
#### MySQL on a VM for Health Informatics:
- **Virtualization in the Cloud**: Importance in healthcare for data segregation, scalability, and recovery.
- **Setting up MySQL**: A healthcare-specific walkthrough, with emphasis on HIPAA-compliant configurations.
- **Securing MySQL**: Configurations, tuning, and enhanced security considerations for protecting sensitive patient data.

#### Connection Pooling in Healthcare Web Apps:
- **Understanding Connection Pools**: Their importance in fast, secure data access.
- **Healthcare App Considerations**: Max connections, wait times, and implications for apps managing healthcare data.
- **Serverless Environments**: Connection pooling in serverless/static environments like Vercel, with potential issues and their impact in a healthcare context.

#### Database Migrations for Patient Data:
- **Why Migrations?**: Understanding their role in evolving healthcare apps without compromising data.
- **Python Migration Tools**: Introduction to Alembic with a focus on health data migration scenarios.
- **Migration Workflow**: Writing, applying, and safely rolling back migrations, while ensuring data integrity and compliance.
- **CI/CD in Healthcare**: Integrating migrations into a CI/CD pipeline with patient data safety and compliance checks.

### Resources:
- [Alembic](https://github.com/sqlalchemy/alembic)
- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)
- [GCP: HIPAA Compliant Cloud SQL Setup](https://datica-2019.netlify.app/academy/google-cloud-sql-guide-how-to-configure-gcp-cloud-sql-to-comply-with-hipaa/)
- [Azure Security Features for MySQL](https://learn.microsoft.com/en-us/azure/mysql/concepts-security)

### Homework:
- [Assignment 4](WK4/assignment4.md)


---

## 5. **Healthcare App Frontend and Styling**
### Lecture Topic:
- Crafting user-friendly interfaces with HTML, CSS, and Tailwind
- Ensuring fast and secure data delivery using Content Delivery Networks (CDN)

### Subtopics:
- **Tailwind for Healthcare UIs**: Integrating Tailwind with Flask to create intuitive, user-friendly healthcare interfaces.
- **Understanding CDNs**: Principles and benefits in the context of health data — ensuring fast, consistent, and secure access.
- **Google Cloud CDN in Healthcare Apps**: Setting up Google Cloud CDN for hosting and delivering static assets, with emphasis on data encryption, cache invalidation, and access controls.
- **Forms in Healthcare**: Designing and implementing secure forms for patient data and medical information entry.
- **Displaying Results**: Presenting search results with styled components while ensuring readability and clarity for medical data.
- **Organizing Static Assets**: Best practices in a healthcare app context, including ensuring assets don't contain PHI (Protected Health Information) and are stored in compliance with regulations.
- **Web Accessibility**: Designing interfaces that are accessible to all users, including those with disabilities — a vital aspect in health applications.

### Azure/GCP Resources:
- [Tailwind](https://v2.tailwindcss.com/docs)
- [Google Cloud CDN](https://cloud.google.com/cdn)
- [Google Cloud CDN with Flask](https://cloud.google.com/appengine/docs/flexible/serving-static-files?tab=python)
- [Web Accessibility for Health Apps](https://ahimafoundation.org/research/the-critical-role-of-web-accessibility-in-health-information-access-understanding-and-use/)
- [Individual Access to Use of Patient Portals and Smartphone Health Apps, 2020](https://www.healthit.gov/data/data-briefs/individuals-access-and-use-patient-portals-and-smartphone-health-apps-2020)

### Homework:
- [Assignment 5](WK5/assignment5.md)


---

## 6. **Healthcare API Endpoints with Flask and FastAPI**
### Lecture Topic:
- Designing RESTful APIs tailored for health informatics using Flask and FastAPI
- Embracing the OpenAPI Specification for healthcare data interoperability

### Subtopics:
- **RESTful API Architecture in Healthcare**:
  - Fundamentals: resources, methods, and status codes tailored for medical data
  - Considerations for patient data: granularity, querying, and data retrieval
- **Flask for Healthcare APIs**:
  - Using Flask-RESTful for creating endpoints with a focus on health data structures
- **FastAPI in Health Informatics**:
  - Benefits of FastAPI: speed, automatic validation, OpenAPI Specification, and its implications for healthcare
  - Crafting endpoints that cater to medical and patient data
  - Generating and leveraging the OpenAPI specification, especially for FHIR integration
- **Exploring OpenAPI in Healthcare**:
  - Importance of OpenAPI for healthcare data interoperability and its role in Azure API Management
  - Adhering to standards: understanding FHIR and its relationship with OpenAPI
- **Securing Healthcare APIs**:
  - Emphasis on HIPAA-compliant measures: rate limiting, API keys, JWT tokens, OAuth2, encryption at rest and in transit

### Python Packages:
- Flask-RESTful: Creating RESTful APIs in Flask
- FastAPI: Crafting APIs with built-in OpenAPI Specification
- Pydantic: Data validation and serialization, with a focus on medical data types
- Uvicorn: ASGI server essential for running FastAPI applications

### Resources:
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [Fast API](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [Azure API Management](https://azure.microsoft.com/en-us/services/api-management/)
- [Azure API Management - Understanding](https://learn.microsoft.com/en-us/azure/api-management/)
- [Azure API Management - Tutorial](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish)
- [FHIR Basics](https://www.hl7.org/fhir/overview.html)

### Homework:
- [Assignment 6](WK6/assignment6.md)


---

## 7. **User Authentication and Management in Healthcare Applications**
### Lecture Topic:
- Implementing secure user registration, authentication, and identity management tailored for healthcare web applications

### Subtopics:
- **Healthcare-centric User Authentication**:
  - Emphasizing the importance of secure authentication in health informatics
  - HIPAA considerations during authentication
  - Best practices for password hashing, storage, and multi-factor authentication (MFA) in healthcare systems
- **Session Management with Healthcare Data**:
  - Introduction to sessions: understanding the nuances of persistent vs. non-persistent sessions in healthcare contexts
  - Securely managing user sessions using `flask_session` with a focus on health data
- **Identity Management in Healthcare Web Apps**:
  - Deep dive into `identity` and `identity.web` for Flask
  - Addressing authentication flow nuances specific to patient and healthcare provider data
  - Importance of role-based access control (RBAC) in health systems
- **Transition to Cloud for Healthcare Authentication**:
  - Benefits of utilizing managed identity platforms, especially concerning HIPAA and HITRUST requirements
  - Integrating Azure Active Directory B2C and Google Cloud Identity Platform with Flask, focusing on health applications
  - Addressing SSO (Single Sign-On) in health systems: benefits and challenges

### Azure/GCP Resources:
- [Azure Active Directory B2C](https://azure.microsoft.com/en-us/services/active-directory-b2c/)
- [Google Cloud Identity Platform](https://cloud.google.com/identity-platform)
- [Azure Managed Identity for Healthcare Apps](https://learn.microsoft.com/en-us/azure/active-directory/develop/scenario-web-app-sign-user-overview?tabs=python)

### Python Packages:
- Flask-Session: For securely managing sessions in Flask applications
- Identity: Integrating authentication and identity with Flask
- Requests: For making HTTP requests securely

### Homework:
- [Assignment 7](WK7/assignment7.md)



---

## 8. **Deployment in Health Informatics**
### Lecture Topic:
- Tailored deployment strategies and platforms for Flask and FastAPI applications in healthcare with a special focus on Docker for standardizing deployment.

### Subtopics:
- **Deployment Considerations in Health Informatics**:
  - Importance of high availability and scalability in health systems
  - Ensuring HIPAA compliance in deployment environments
  - Security measures: encryption at rest and in transit, private networks, and secure storage
- **Introduction to Docker in Health Informatics**:
  - Understanding Docker and containerization.
  - The role of Docker in ensuring efficient, consistent, and secure deployment.
- **Dockerizing Flask/FastAPI Applications**:
  - Creating Dockerfiles and building Docker images for health applications.
  - Running and managing Docker containers.
- **Docker Compose in Multi-Container Environments:**
  - Using Docker Compose for managing multi-container setups.
  - Orchestrating multiple services like Flask applications and databases.
- **Serverless Deployment with Vercel**:
  - Introduction and benefits of Vercel's static site deployment services
  - Deploying Flask/FastAPI apps as serverless functions on Vercel with an emphasis on handling health data
- **Integration and Deployment in Healthcare (CI/CD)**:
  - CI/CD's significance in healthcare web application development
  - Using GitHub Actions for automated deployment and testing: ensuring patient data security and privacy
- **Deployment on Google Cloud Run and Azure App Service**:
  - Special considerations for deploying health informatics applications
  - Monitoring and auditing tools for compliance purposes
  - Scaling strategies specific to health application demands
- **Advanced Deployment with Docker**:
  - Introduction to Docker with an emphasis on health informatics apps
  - Best practices for containerizing Flask/FastAPI applications handling health data
  - (Optional) Advanced security measures using Azure Container Apps for healthcare systems

### Azure/GCP Resources:
- [Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python)
- [Google Cloud Run](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service)
- [Azure Container Apps](https://learn.microsoft.com/en-us/azure/developer/python/tutorial-containerize-simple-web-app)
- [Vercel Deployment for Python Flask](https://github.com/vercel/examples/tree/main/python/flask)
- [GitHub Actions for Applications](https://docs.github.com/en/actions/guides/building-and-testing-python)
- [GitHub Actions for Python with Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/deploy-github-actions?tabs=applevel)

### Homework:
- [Assignment 8](WK8/assignment8.md)


---

## 9. **Logging, Monitoring, and Debugging in Health Informatics**
### Lecture Topic:
- Criticality and methodologies of logging, monitoring, and debugging in health-focused Python applications.

### Subtopics:
- **Medical Systems and the Imperative of High Availability**:
  - Real-world implications of system outages in healthcare.
  - The regulatory need for robust logging and monitoring.
- **Python Logging Basics**:
  - Introduction to Python's built-in [`logging`](https://docs.python.org/3/library/logging.html) module.
  - Differentiating logging levels (INFO, DEBUG, ERROR, etc.) in medical scenarios.
  - Customizing and directing log outputs, ensuring PHI (Protected Health Information) is secure.
- **Enhanced Logging with Third-party Tools**:
  - [Loguru](https://github.com/Delgan/loguru): Enhanced logging capabilities and clean presentation.
  - [Sentry](https://sentry.io): Catching and responding to real-time errors.
  - [Graylog](https://www.graylog.org) & [ELK Stack](https://www.elastic.co/what-is/elk-stack): Centralizing and visualizing logs.
  - [structlog](https://www.structlog.org/en/stable/): Creating and analyzing structured logs.
- **Debugging & Tracing in a Healthcare Context**:
  - Tracing's significance in distributed health systems.
  - Python debugging tools tailored for cloud applications.
  - Best practices in debugging health informatics apps.
- **Performance Monitoring in Medical Apps**:
  - Identifying vital performance metrics for medical applications.
  - Setting up responsive alerts for high-priority incidents.
  - Monitoring patient data access and ensuring HIPAA compliance.
- **Advanced Cloud-based Tools for Medical Apps**:
  - Introduction to the nuances of distributed tracing in health systems.
  - Integrating Flask and FastAPI with Azure and GCP's logging and monitoring services.
  - Premium platforms for health application surveillance and performance insights.

### Resources:
- [Azure Monitor and Log Analytics](https://azure.microsoft.com/en-us/services/monitor/)
- [Google Cloud Monitoring and Logging](https://cloud.google.com/products/operations)
- [OpenCensus](https://opencensus.io)
- [Azure Monitor's Integration with Opencensus-Python](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opencensus-python)

### Homework:
- [Assignment 9](WK9/assignment9.md)

---

## 10. **Scaling and Performance Optimization**
### Lecture Topic:
- Strategies and methodologies for scaling Flask applications and optimizing performance.

### Subtopics:
- **Fundamentals of Scaling**:
  - Contrasting horizontal vs. vertical scaling.
  - The scaling advantage of stateless applications over stateful ones.
- **Load Balancing in Depth**:
  - The critical role of load balancers in achieving scalability.
  - Exploring application-layer vs. network-layer load balancing.
  - Understanding sticky sessions and their implications.
  - Emphasizing health checks for service continuity.
- **Database Scalability Challenges**:
  - Navigating the complexities of scaling relational databases.
  - Introduction to advanced techniques like sharding and replication.
  - The power and pitfalls of database caching.
- **Enhancing Flask Application Performance**:
  - Identifying and remedying performance bottlenecks in Flask apps.
  - Utilizing profiling tools tailored for Flask.
  - Tweaking Flask configurations for optimal results.
- **Cache Strategies and Tools**:
  - Diving deep into caching mechanisms for web applications.
  - Harnessing caching solutions like Redis and Memcached for rapid data retrieval.
  - Discussing cache eviction policies and common pitfalls.
- **Auto-scaling: A Double-edged Sword**:
  - Using key metrics to guide auto-scaling decisions.
  - Hands-on with auto-scaling setups in popular cloud platforms.
  - Evaluating the benefits and challenges of auto-scaling.
- **Microservices: The Future of Scalability**:
  - Decomposing monolithic architectures into flexible microservices.
  - An introduction to the world of service orchestration and the Docker ecosystem.

### Python Tools to Test Performance:
#### 1. **Locust.io**:
- **Description**: An open-source, Python-based tool that simulates user behavior and load-tests web applications for scalability.
- **Website**: [Locust.io](https://locust.io/)
#### 2. **Flask-Testing**:
- **Description**: A Flask-specific testing utility. Perfect for combination with `pytest` to comprehensively test Flask applications.
- **Website**: [Flask-Testing on PyPi](https://pypi.org/project/Flask-Testing/)
#### 2. **PyTest**:
- **Description**: The `pytest` framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.
- **Website**: [Pytest on PyPi](https://pypi.org/project/pytest/)

### Azure/GCP Resources:
- [Azure Load Balancer](https://azure.microsoft.com/en-us/services/load-balancer/)
- [Google Cloud Load Balancing](https://cloud.google.com/load-balancing)
- [Azure Kubernetes Service](https://azure.microsoft.com/en-us/services/kubernetes-service/)
- [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)

### Homework:
- [Assignment 10](WK10/assignment10.md)


---

## 11. **Health Data Storage Solutions**
### Lecture Topic:
- Efficient and secure data storage solutions tailored for health informatics.

### Subtopics:
- **Blob/General Storage vs. Databases**:
  - Unraveling the intricacies of blob/general storage and databases.
  - Pinpointing specific use-cases for general storage and databases in health informatics.
- **Local Storage vs. Cloud Storage**:
  - Delving into the merits and demerits of local and cloud storage solutions.
  - Scrutinizing the security implications of both storage types in a healthcare context.
- **Cost-effectiveness of Cloud Storage**:
  - Decoding the pricing structures of major cloud storage providers.
  - Exploring potential cost-saving strategies for health data storage in the cloud.
- **Flask and Health Data**:
  - Techniques for securely uploading, retrieving, and storing health data in Flask applications.
  - Addressing data compliance and regulations (like HIPAA) while handling health data in Flask.
- **Securing Health Data in Storage**:
  - Importance of encryption (both in-transit and at-rest) for health data.
  - Overview of Identity and Access Management (IAM) policies tailored for health data.
- **Health Data Redundancy and Backups**:
  - Strategies for ensuring high availability and disaster recovery of health data.
  - Importance of versioning and maintaining health data integrity.

### Azure/GCP Resources:
- [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/)
- [Azure Security and Compliance: Blueprints for HIPAA/HITRUST](https://azure.microsoft.com/en-us/services/blueprints/hipaa-hitrust/)
- [Google Cloud Storage](https://cloud.google.com/storage)
- [GCP Health-specific Compliance and Security](https://cloud.google.com/solutions/healthcare-life-sciences)

### Homework:
- [Assignment 11](WK11/assignment11.md)


---

## 12. **Health Data Security Best Practices**
### Lecture Topic:
- Implementing stringent security measures for Flask applications handling health data.

### Subtopics:
- **Environment Files and Token Management**:
  - Delving into the nuances of `.env` files and their role in concealing tokens and keys.
  - Best practices for environment variable management and access.
- **Deployment Security**:
  - Understanding the risks during deployment and ensuring tokens and keys remain concealed.
  - Continuous monitoring post-deployment to detect and counter threats.
- **Data Encryption in Health Informatics**:
  - In-depth exploration of data encryption methods: at-rest and in-transit.
  - Encryption best practices tailored for health data.
- **Advanced Security Testing**:
  - Techniques for preventing subdomain enumeration.
  - Strategies to counteract ransomware threats, especially targeting health data.
  - Safeguarding applications against password attacks: Brute force, dictionary attacks, and more.
- **Capitalizing on Cloud Security**:
  - Exploring the automatic security features and tools provided by Azure and GCP.
  - Diving deep into firewall configurations, VPNs, private networks, and their significance in protecting health data.
- **Shared Responsibility in Cloud**:
  - Understanding the demarcation between cloud provider responsibilities and user responsibilities.
  - Emphasizing the importance of compliance, regular audits, and certifications in health data storage and transfer.
- **Healthcare Security Regulations and Compliance**:
  - Introduction to HIPAA and its significance.
  - Ensuring that Flask applications and databases are HIPAA compliant.

### Azure/GCP Resources:
- [Azure Security Center](https://azure.microsoft.com/en-us/services/security-center/)
- [Azure Compliance: HIPAA/HITRUST](https://azure.microsoft.com/en-us/services/blueprints/hipaa-hitrust/)
- [Google Cloud Security Command Center](https://cloud.google.com/security-command-center)
- [Google Healthcare Data Protection Toolkit](https://github.com/GoogleCloudPlatform/solution-acceleration-toolkit)

### Python Libraries:
- [Flask-Talisman](https://github.com/GoogleCloudPlatform/flask-talisman): Provides security headers for Flask applications.
- [Flask-Security](https://github.com/Flask-Middleware/flask-security/): Simplifies common security mechanisms for Flask.

### Homework:
- [Assignment 12](WK12/assignment12.md)


---

## 13. **Serverless in Health Informatics**
### Lecture Topic:
- Embracing serverless architectures and event-driven computing in health informatics

### Subtopics:
- **Basics of Serverless**:
  - Grasping the concept of serverless and its significance: Diving into FaaS (Function as a Service).
  - Exploring real-world healthcare scenarios benefitting from serverless architectures.
- **Building Health Functions**:
  - Crafting cloud functions in Python tailored for health data processing.
  - Examples: Automated patient data updates, sending notifications for abnormal health metrics, etc.
- **Integration into Healthcare Systems**:
  - Seamlessly weaving serverless functions into existing health informatics applications.
  - Case Study: Integrating a serverless function to send SMS alerts for critical patient updates.
- **Serverless Triggers in Health Data Streams**:
  - Deep diving into triggers and bindings specific to healthcare events.
  - Demonstrating real-time health metric capture using serverless.
- **Cost-Efficiency in Health Informatics**:
  - Elaborating on the benefits of serverless: Cost savings, dynamic scalability, and minimal management.
  - Potential reductions in IT infrastructure costs for healthcare organizations.
- **Serverless Drawbacks in Healthcare**:
  - Understanding the challenges: Cold starts, state management, and the risk of vendor lock-in.
  - Weighing the pros and cons: When to opt for serverless in health informatics and when not to.

### Azure/GCP Resources:
- [Azure Functions](https://azure.microsoft.com/en-us/services/functions/)
- [Azure Functions Python Developer Guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
- [Google Cloud Functions](https://cloud.google.com/functions)

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
