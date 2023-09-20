---
marp: true
theme: default
paginate: true
---

<!-- _class: lead -->

# Introduction to SQL Commands

**Hants Williams, PhD, RN**

---

## What is SQL?

- Structured Query Language
- Standardized language for managing and manipulating databases
- Critical for handling healthcare data securely and efficiently

---

- **DDL (Data Definition Language)**
  - Deals with database structures/schema.
  - Commands: `CREATE`, `ALTER`, `DROP`

- **DML (Data Manipulation Language)**
  - Deals with data manipulation and storage.
  - Commands: `INSERT`, `UPDATE`, `DELETE`

- **DQL (Data Query Language)**
  - Deals with querying and retrieving data.
  - Command: `SELECT`

- **DCL (Data Control Language)**
  - Deals with permissions and data access controls.
  - Commands: `GRANT`, `REVOKE`

---

## Basic SQL Commands

1. `SELECT` - DQL 
2. `INSERT` - DML 
3. `UPDATE` - DML  
4. `DELETE`  - DML 
5. `CREATE` - DDL 
6. `DROP` - DDL 
7. `ALTER` - DDL 

---

## CREATE

Create tables for healthcare data.

```sql
CREATE TABLE tablename (
  column1 datatype,
  column2 datatype
);
```

Example:

```sql
CREATE TABLE patients (
  patient_id INT PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  birthdate DATE,
  diagnosis TEXT
);
```

---

## Common SQL Data Types

Here are some commonly used data types:

- **INTEGER**: Whole numbers (e.g., -3, 0, 42).
  
- **REAL**: Floating-point numbers (e.g., -3.14, 0.001, 42.0).
  
- **TEXT**: Strings of characters (e.g., "Hello", "Patient Name").

- **DATE**: Dates in the format `YYYY-MM-DD` (e.g., `2023-09-18`).
  
- **TIME**: Time in the format `HH:MM:SS` (e.g., `14:30:00`).

- **DATETIME**: Combination of date and time (e.g., `2023-09-18 14:30:00`).

- **BLOB**: Binary data, like images or files.

Note: The exact naming and behavior of these types might vary slightly depending on the database system (*mySQL* vs *Sqlite* vs *MS SQL Server*).

---

## INSERT

Add new patient records.

Template: 

```sql
INSERT INTO tablename (column1, column2)
VALUES (value1, value2);
```

Example:

```sql
INSERT INTO patients (first_name, last_name, diagnosis)
VALUES ('Jane', 'Smith', 'Hypertension');
```

---

## SELECT

Retrieve patient data.

Template: 

```sql
SELECT column1, column2
FROM tablename
WHERE condition;
```

Example:

```sql
SELECT first_name, last_name, diagnosis
FROM patients
WHERE diagnosis = 'Diabetes';
```

---



## UPDATE

Modify patient records.

Template: 

```sql
UPDATE tablename
SET column1 = value1, column2 = value2
WHERE condition;
```

Example:

```sql
UPDATE patients
SET diagnosis = 'Hyperthyroidism'
WHERE patient_id = 12345;
```

---

## DELETE

Remove patient records.

```sql
DELETE FROM tablename
WHERE condition;
```

Example:

```sql
DELETE FROM patients
WHERE patient_id = 12345;
```



---

## DROP

Delete old or redundant healthcare tables.

```sql
DROP TABLE tablename;
```

Example:

```sql
DROP TABLE old_patient_records;
```

---

## ALTER

Modify the structure of patient tables.

```sql
ALTER TABLE tablename ADD COLUMN columnname datatype;
```

Example:

```sql
ALTER TABLE patients ADD COLUMN phone_number TEXT;
```

---

<!-- _class: lead -->

# Conclusion

- SQL provides the tools to manage and query healthcare data that lives in a relational DB.
- Commands can become complex 
- ...tip of the iceberg 

---


## Official MySQL 8.0 Database Developer Professional
- For students: [Oracle Academy Course](https://education.oracle.com/oracle-database-foundations-novice-level-exam/pexam_1Z0-006)
  - [DB Foundations](https://academy.oracle.com/en/solutions-curriculum.html) OR 
  - [DB and Programmign with SQL](https://academy.oracle.com/pages/database_design_course.pdf)
- More advanced: [Oracle University](https://mylearn.oracle.com/ou/learning-path/earn-the-mysql-80-database-developer-certified-professional-credential/82110/)
  - I would recommend focusing on the 'developer' path, as that involves actually creating tables/building queries/etc...
  - [Other MySQL Certification Paths](https://education.oracle.com/oracle-certification-path/pFamily_406)

---

## Cloud-focused: 
- Azure: This focuses more so on the deployment and underpinnings of a SQL server. [Azure SQL fundamentals](https://learn.microsoft.com/en-us/training/paths/azure-sql-fundamentals/)

---

## Free interactive SQL learning tutorials to practice: 
- CodeAcademy: [Learn SQL](https://www.codecademy.com/learn/learn-sql)
- Mode: [SQL Tutorial for Data Analysis](https://mode.com/sql-tutorial/introduction-to-sql)
- SQLZoo: [Learn SQL Step by Step](https://sqlzoo.net/wiki/SQL_Tutorial)
- SqlBolt: [20 Lessons](https://sqlbolt.com/)
- SqlPractice: [Hospital.DB Practice Environment](https://www.sql-practice.com/)
- W3: [W3 Schools Tutorial SQL](https://www.w3schools.com/sql/default.asp) 


