## **Week 4 Homework Assignment: MySQL on Cloud Platforms - Azure and GCP**

### **Objective**:
This assignment focuses on MySQL, and exploring its implementation on leading cloud platforms: Azure and GCP. By the end, you'll gain hands-on experience in setting up MySQL on these platforms, using MySQL Workbench to design, manage, and interact with your databases, and optionally connecting to your database using Python to retrieve data.

### **Instructions**:

#### **1. MySQL Setup on Azure and GCP**:
- Spin up an instance of MySQL on both Azure and GCP. Be sure to use the lowest cost options. 
- Make sure that the instance is properly configued to allow inbound traffic from the world wide web. 

#### **2. MySQL Workbench for Database Interaction**:
- Install and configure MySQL Workbench on your local machine.
- Connect MySQL Workbench to the MySQL instances you set up in step 1.
- Based off my provided SQL scripts in the WK4/code folder, generate an Entity-Relationship Diagram (ERD) for your databases using MySQL Workbench. You must create at least one new table, with at least 3 fields, that contains a primary key and a foreign key that connects it to another table. You can create the same data in both instances on Azure and GCP. 

#### **3. OPTIONAL BUT HIGHLY RECOMMENDED: Python Script for Database Interaction**:
- Write a Python script that connects to your MySQL database. Please use my script as a example in WK4/code/python_connectionExample.py 
- Then using pandas, create some fake dumy data for each of the tables in your databases. Push the data into them. 
- Then retrieve data from one of the tables and store it in a Pandas DataFrame.
- Document the process, including the libraries used, the connection method, and any challenges faced.
- If you do this step, be sure to use a .ENV file to store your connection keys, and .gitignore to avoid sharing the .ENV file with github

#### **4. Documenting Code Errors**:
- If you encounter any errors or challenges in any step, it's vital to document them meticulously.
  - Take screenshots or create screencasts/recordings showcasing the issue.
  - Describe the steps leading up to the error and any troubleshooting or modifications you attempted.
  - Elucidate what you believe to be the root cause, even if you're uncertain. This helps in understanding your approach.
  - Remember that facing and resolving errors is a significant part of the learning journey. Thorough documentation is key.

### **Submission**:
- Create a new GitHub repository named `mysql_cloudmanaged_databases` in your GitHub account.
- Populate your repository with:
  - Your MySQL setup documentation for both Azure and GCP.
  - Your ERD generated with MySQL Workbench.
  - SQL commands executed and their outcomes.
  - Optionally, your Python scripts and a Jupyter notebook detailing your database interaction.
  - Screenshots, videos, or any other visual aids showcasing your application, especially any documented errors.
  - A comprehensive README.md file, detailing:
    - The setup process on both Azure and GCP.
    - Your experience with MySQL Workbench, including the ERD creation and database interactions.
    - Optionally, your Python to database interaction approach and findings.
    - Documented code errors and your troubleshooting attempts.
    - Any other important documentation or guidelines.
- Submit the link to your repository as your assignment submission.
- Ensure your repository is public for accessibility during review.

**Tip**:  **BE SURE TO USE .ENV FILE IN YOUR REPO AND .GITIGNORE TO AVOID SHARING YOUR SECURITY KEYS**. Prioritize security! Properly secure your MySQL instances and never expose sensitive credentials or data.