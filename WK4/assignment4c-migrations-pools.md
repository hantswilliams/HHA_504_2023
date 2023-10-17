## **Databases Part 4c Assignment: Cloud Database Management with Connection Pooling and Migrations**

### **Objective**:
Gain practical experience in managing a cloud-based MySQL database with a focus on implementing connection pooling and performing database migrations. You will work with both Azure and Google Cloud Platform (GCP) for this assignment.

### **Instructions**:

#### **1. Connection Pooling Setup**:
- **Azure**: Spin up an Azure MySQL Database instance.
- **GCP**: Create a Google Cloud SQL MySQL instance.
- Configure connection pooling for the Azure databases.
  - Define appropriate pool size and timeout settings.
    - `max_connections`: 20
    - `connect_timeout`: 3 

**Reminder**: Please be sure that the appropriate network/firewall rules are established to ensure inbound/outbound traffic to your database on either Azure or GCP.

#### **2a. Database Schema and Data**:
- **Azure**: Create a database schema with at least two tables on your Azure MySQL instance.
- **GCP**: Create an equivalent database schema with the same structure on your Google Cloud SQL MySQL instance.
- Populate the tables with sample data.
  - Ensure there is a foreign key relationship between the tables.
  - Document the schema structure and data population process for both Azure and GCP instances.
- For GCP example: https://github.com/hantswilliams/HHA_504_2023/blob/main/WK4/code/migrations/gcp.py 
- For Azure example: https://github.com/hantswilliams/HHA_504_2023/blob/main/WK4/code/migrations/azure.py 

#### **2b. Using MySQL Workbench to Generate ERD**:
- Launch MySQL workbench adn connect it to your mySQL instance
- Using the 'reverse engineer' function, retrieve the database schema structure 
- Modify the schema to ensure the foreign key relationship is properly documented
- Generate an ERD for your database using MySQL Workbench and save a photo of it in your repo

#### **3. SQLAlchemy and Flask Integration**:
- Modify or create a Python Flask application to connect to both the Azure and GCP MySQL databases.
- Implement SQLAlchemy for connection pooling in the Flask application.
- Develop endpoints to retrieve and display data from both databases.
- Ensure the Flask application works seamlessly with both databases.
- Provide screenshots or videos showcasing the Flask application connected to Azure and GCP databases.

#### **4. Database Migrations with Alembic**:
- Set up Alembic for database migrations on both Azure and GCP MySQL instances.
- Create an initial migration script for each database to capture the current schema.
- Implement a migration that alters the schema in a meaningful way (e.g., add a new table or modify an existing one) for both databases.
- Run the migrations and document the process, including any challenges faced and how you resolved them.

#### **5. Documentation and Error Handling**:
- Prepare a detailed README.md file in your GitHub repository:
  - Explain the setup and configuration of connection pooling for Azure and GCP databases.
  - Describe the database schema structure, including the rationale behind it.
  - Document the steps and challenges encountered during the database migration process.
  - Include screenshots or videos demonstrating the Flask application's interaction with both databases.
- If you encounter any errors or challenges, document them thoroughly, providing screenshots, descriptions of your troubleshooting steps, and potential root causes.

### **Submission**:
- Create a new GitHub repository named `cloud_db_mgmt_pooling_migrations` in your GitHub account.
- Include all your code, scripts, and documentation in the repository.
- Share the link to your repository as your assignment submission.
- Ensure your repository is public so that it's accessible for review.

**Tip**: Pay special attention to security when managing cloud-based databases. Never expose sensitive credentials or data, and use secure practices throughout the assignment.