## **Week 3 Homework Assignment: Introduction to Databases with SQLite**

### **Objective**:
Introduction to the world of databases, starting with SQLite. Integrate data processing with Python, utilize Pandas for exploratory data analysis, and conduct database operations using SQLite.

### **Instructions**:

#### **1. Data Exploration and Analysis**:
- Import pricing transparency datasets from at least two different hospital systems into a Pandas DataFrame.
  - Conduct a basic exploratory analysis using Python, focusing on aspects such as data distribution, missing values, and basic statistics.
  - Document any captivating insights or observations derived from your analysis.
  - Expection is to have at least basic descriptive statistics for numerical columns, and frequency counts for categorical columns

#### **2. SQLite Database Operations**:
- Establish a local SQLite database.
- Implement the `to_sql` function from Pandas to transfer your DataFrame's data into the SQLite database.
  - Ensure your tables possess the correct structure and that the data types are correct

#### **(Optional) Dive Deeper with SQL**:
- Draft at least one custom `select` SQL query to perform a rudimentary analysis on the data within your SQLite database.
  - For instance, explore patterns in pricing for a specific code (CPT) across different insurances
- Document the SQL queries you've written, the subsequent results, and any conclusions or insights that emerge from them.

### **Submission**:
- Initiate a new GitHub repository titled `sqlite_database_operations` in your GitHub account.
- Leverage components of code from prior assignments where necessary.
- Configure your GitHub repository to include:
  - Python scripts illustrating your exploratory data analysis and database transactions.
  - SQL scripts containing your custom SQL queries and analysis (if you embarked on the optional task).
  - A comprehensive README.md file that provides:
    - Details on the datasets you've selected.
    - An account of the exploratory data analysis process.
    - Instructions to replicate your SQLite database setup.
    - Any other pertinent documentation or guidelines.
- Present the URL of your repository as your assignment submission.
- Confirm that your repository is public to ensure it's available for evaluation.

**Tip**: The process of data preprocessing prior to its transfer to any database is crucial. Not only does it guarantee data accuracy, but it also fosters efficient storage and querying.

