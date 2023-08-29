## **Week 3 Homework Assignment: Introduction to Databases with SQLite and Cloud SQL Services**

### **Objective**:
Get a deep dive into databases, starting with SQLite, and gradually move on to cloud SQL services. You'll integrate data processing with Python, use Pandas for exploratory data analysis, and handle database operations with both SQLite and cloud databases.

### **Instructions**:

#### **1. Data Exploration and Analysis**:
- Import pricing transparency datasets from at least two different hospital systems into a pandas DataFrame.
  - Conduct a basic exploratory analysis using Python, looking at things like data distribution, missing values, and basic statistics.
  - Document any interesting insights or observations from your analysis.

#### **2. SQLite Database Operations**:
- Set up a local SQLite database.
- Use the `to_sql` function from pandas to transfer data from your DataFrame to the SQLite database.
  - Make sure your tables are correctly structured and the data types are appropriate for efficient queries.

#### **3. Moving to the Cloud: Azure SQL Database & Google SQL Server**:
- Push your cleaned and preprocessed data to databases in both:
  - Azure SQL Database
  - Google SQL Server
- Provide the connection string (without credentials) or database URL for verification.
  - Ensure proper security measures: don't expose any sensitive data or credentials.

#### **(Optional) Dive Deeper with SQL**:
- Write custom SQL queries to conduct a basic analysis on the data you've pushed to Azure and GCP databases.
  - For example, you might look for patterns in pricing across different hospital systems, or anomalies in the data that could indicate errors or interesting events.
- Document your SQL queries, the results, and any conclusions or insights drawn from them.

### **Submission**:
- Create a new GitHub repository named `flask_4_cloud_mysql_flask` in your GitHub account.
- Feel free to re-use parts of your code from prior assignments where necessary 
- Prepare your GitHub repository:
  - Your Python scripts detailing your exploratory data analysis and database operations.
  - SQL scripts with your custom SQL queries and analysis (if you chose the optional task).
  - A detailed README.md file, outlining:
    - The datasets you've chosen.
    - The process of exploratory data analysis.
    - Steps to replicate your SQLite, Azure, and GCP database setups.
    - Any other relevant documentation or instructions.
- Share the link to your repository as your assignment submission.
- Ensure your repository is public so that it's accessible for review.

**Tip**: Remember the importance of data preprocessing before pushing to any database. This not only ensures data integrity but also optimizes for efficient storage and querying.

