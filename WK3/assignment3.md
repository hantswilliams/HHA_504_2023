## **Week 3 Homework Assignment: Introduction to Databases with SQLite**

### **Objective**:
Introduction to the world of databases, starting with SQLite. Integrate data processing with Python, utilize Pandas for exploratory data analysis, and conduct database operations using SQLite.

### **Instructions**:

#### **1. Data Exploration and Analysis**:
1.1 Import pricing transparency datasets from at least two different hospital systems into a Pandas DataFrame. You can use one of the examples provided in the WK3/data folder, or try finding a hospital on your own. The google search approach I used to find these ones was: `{hospital name} price transparency machine readible` - replacing hospital name with the name of the hospital you want to find data for. There will typically be a page that contains download links for a .CSV, .JSON, or .XLS(X) file.  
  - Conduct a basic exploratory analysis using Python, focusing on aspects such as data distribution, missing values, and basic statistics.
  - Document any captivating insights or observations derived from your analysis.
  - My expection is to have at least basic descriptive statistics for numerical columns, and frequency counts for categorical columns

#### **2. SQLite Database Operations**:
2.1 Create a local SQLite database called `health.db`

2.2 *Manual table creation*: Manually create a table (schema) using `CREATE TABLE` SQL query. The table should contain at least 5 columns. Please have at least two columns be numerical columns, and two columns should be categorical (string) columns. Then write at least one `INSERT INTO` SQL query to populate 1 or 2 rows worth of fake data. 

2.3. *Automatic table creation*: Implement the `to_sql` function from Pandas to take the example data from Part 1 of this assignment into the SQLite database.

#### **(Optional) Dive Deeper with SQL**:
- Draft at least one custom `select` SQL query to perform a rudimentary analysis on the data within your SQLite database.
  - For instance, explore patterns in pricing for a specific code (CPT) across different insurances
- Document the SQL queries you've written, the subsequent results, and any conclusions or insights that emerge from them.

### **Submission**:
- Initiate a new GitHub repository titled `sqlite_database_operations` in your GitHub account.
- Leverage components of code from prior assignments where necessary.
- Configure your GitHub repository to include:
  - Python scripts (or colab notebook) illustrating your exploratory data analysis and database transactions.
  - Your custom SQL queries and analysis (if you embarked on this optional task).
  - A comprehensive README.md file that provides:
    - Details on the datasets you've selected.
    - An account of the exploratory data analysis process.
    - Instructions to replicate your SQLite database setup.
    - Any other pertinent documentation or guidelines.
- Present the URL of your repository as your assignment submission.
- Confirm that your repository is public to ensure it's available for evaluation.

**Tip**: The process of data preprocessing prior to its transfer to any database is crucial. Not only does it guarantee data accuracy, but it also fosters efficient storage and querying.

