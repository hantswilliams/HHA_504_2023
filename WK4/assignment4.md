## **Week 4 Homework Assignment: MySQL on VMs with Azure and GCP**

### **Objective**:
This week's assignment is all about diving deeper into databases, specifically MySQL, and understanding the nuances of running a database on a cloud VM. You'll get hands-on experience setting up a MySQL instance on a VM, integrating it with your Flask app, and tackling real-world challenges such as connection pooling and database migrations.

### **Instructions**:

#### **1. MySQL Setup on Azure/GCP VM**:
- Spin up a VM on Azure or GCP.
- Install MySQL on this VM. Ensure it's correctly configured and secured.
- Create a simple database with at least two tables. Populate the tables with sample data.
  - Document the schema you've chosen and why.

#### **2. Integrate with Flask and Implement Connection Pooling**:
- Modify your Flask application (from previous assignments) to connect to this new MySQL instance.
- Implement connection pooling to manage and optimize database connections.
  - Use tools or libraries like SQLAlchemy to facilitate this.
- Simulate various traffic scenarios to your Flask application (e.g., high traffic).
  - Monitor the behavior, especially in terms of database connections.
  - Document your observations: How does the application behave under different traffic conditions? Were there any unexpected behaviors or challenges?

#### **3. Embrace Change with Database Migrations**:
- Introduce a new feature to your Flask application that necessitates changes to your database (e.g., adding a new table or altering an existing one).
- Implement a migration strategy to handle this database change.
  - Consider tools like Alembic or Flask-Migrate.
- Ensure your application and database work seamlessly post-migration.
- Document the steps you undertook for this migration, challenges you faced, and the results of the migration.

#### **4. Documenting Code Errors**:
- Should you encounter errors or challenges that prevent you from completing any section, it's essential to document them.
  - Take screenshots or create screencasts/recordings showcasing the issue.
  - Describe the steps you took leading to the error and any troubleshooting or modifications you attempted.
  - Clearly specify what you believe might be the root cause, even if you're unsure. It helps in understanding your thought process.
  - Remember, encountering and resolving errors is an integral part of the learning process. Your diligence in documenting them is crucial.

### **Submission**:
- Create a new GitHub repository named `flask_4_databases_mysql_vm` in your GitHub account.
- Feel free to re-use parts of your code from prior assignments where necessary 
- Prepare your GitHub repository:
  - Your Python scripts and Jupyter notebooks detailing your MySQL setup, connection pooling implementation, and database migration strategy.
  - Screenshots or videos showcasing the working application, especially during the traffic simulation, post-migration, and any documented errors.
  - A detailed README.md file, outlining:
    - The VM and MySQL setup process.
    - The rationale behind your database schema.
    - Your experience and findings from the connection pooling exercise.
    - Steps and challenges from the database migration process.
    - Documented code errors and your troubleshooting attempts.
    - Any other relevant documentation or instructions.
- Share the link to your repository as your assignment submission.
- Ensure your repository is public so that it's accessible for review.

**Tip**: Security is paramount! Make sure your MySQL instance is properly secured, and never expose sensitive credentials or data.
