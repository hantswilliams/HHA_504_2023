---
marp: true
title: DBs
paginate: true
theme: default
---

<!-- _class: lead -->

# Introduction to Databases: Relational Databases
**Hants Williams, PhD, RN**

---

# Database Learning Progression

---

## 1. SQLite: Grasping the Basics
- **Lightweight, serverless database**
- Understand fundamentals without complex setup or maintenance
- Activities: CRUD operations, simple queries, table creations

---

## 2. Managed MySQL on Cloud Platforms
- **Why Managed?**
    - Ease of setup, automated backups, scalability
- Platforms:
    - **Google Cloud Platform (GCP)**: Cloud SQL for MySQL
    - **Azure**: Azure Database for MySQL
- Activities:
    - Advanced SQL, security, integrating with apps, scalability exercises

---

## 3. Manual MySQL Installation on VM
- Deep dive into the intricacies
- Platforms: VMs on GCP or Azure
- Activities:
    - Setup, user roles, performance tuning, backups, recovery

---

## Key Takeaway
Solid foundation ➡️ Best practices in real-world environments ➡️ Advanced understanding

---

## What is a Database?

- Organized collection of structured information
- Stored electronically in a computer system
- Efficiently retrieves, updates, and manages data

---

## Types of Databases

1. **Relational Databases** (RDBMS)
2. Document-based Databases
3. Key-Value Stores
4. Graph Databases
5. Time-Series Databases

<br />
(Our focus: Relational Databases)

---

## Relational Databases (RDBMS)

- Organized into tables (relations)
- Tables have rows and columns
- Use SQL (Structured Query Language) for interaction

---

## Why Use Relational Databases?

- 1+ person needs to access the data at the same time
- Enforces strict structur, data types, and organization
- Scalable and Flexible
- Security: RBAC
- Support for Complex Queries
- Mature and Established

---

## Tables, Rows, and Columns

- **Table (Relation)**: An entity, e.g., `Patients`
- **Row (Tuple)**: A single record, e.g., a specific patient
- **Column (Attribute)**: A property or characteristic, e.g., `first_name`, `birthdate`

---

## Primary and Foreign Keys

- **Primary Key**: Unique identifier for a record in a table, e.g., `patient_id`
- **Foreign Key**: Links tables together, referencing a primary key in another table

<br />

Example:
- A `Visits` table might have a `patient_id` foreign key to link a visit to a `Patients` table.

---

## Normalization

- Process of structuring data to reduce redundancy
- Ensures data consistency and integrity
- Divides larger tables into smaller ones and links them using relationships

---

## Example of Normalization

Consider a hospital's clinical database with a table tracking which doctors attended to which patients:

Not normalized:

| Patient Name | Doctor Attending     |
|--------------|----------------------|
| John Smith   | Dr. Alice Henderson  |
| Jane Doe     | Dr. Alice Henderson  |
| Tom Brown    | Dr. Bob Matthews     |
| Sarah Connor | Dr. Charlie Anderson |

<br />

What are the potential issues? 

---

## The issues could be...

Issues:
- Repetitive doctor names.
- What if a doctor changes their name or gets a new title? It would require multiple updates.

---

**Normalized Tables 1: Doctors**:

*Doctors Table (using doctor IDs)*:

| Doctor ID | Doctor Name           |
|-----------|-----------------------|
| 001       | Dr. Alice Henderson   |
| 002       | Dr. Bob Matthews      |
| 003       | Dr. Charlie Anderson  |

---

**Normalized Tables 1: Patients**:


*Clinical Attendances Table (using patient names and doctor IDs)*:

| Patient Name | Doctor ID |
|--------------|-----------|
| John Smith   | 001       |
| Jane Doe     | 001       |
| Tom Brown    | 002       |
| Sarah Connor | 003       |

---

## Benefits of Normalization:
- Avoids repetition of doctor names.
- Changes to doctor's information only need to be made in one place.

<br />
By using unique identifiers (Doctor ID) in the normalized tables, we're able to link data without repeating the actual names.


---


## Popular Relational Databases

- **Oracle Database** - not free
- **MySQL** - free 
- **Microsoft SQL Server** - not free 
- **PostgreSQL** - free 
- **SQLite** - free 

---

## Benefits of RDBMS

- **Data Integrity**: Rules and constraints ensure accuracy.
- **Security**: Granular permissions and access controls.
- **ACID Compliance**: Ensures reliability (Atomicity, Consistency, Isolation, Durability).
- **Query Performance**: Optimized for complex queries and operations.

---



## Transactions in Relational Databases

- **Definition**: A transaction is a sequence of one or more SQL operations executed as a single logical unit of work.

- **Purpose**:
  - Ensure data integrity and consistency.
  - Allows multiple operations to be treated as one, ensuring that either all succeed or none do.

---

## Transaction Example:

- **Example Scenario**:
  - Consider a healthcare application:
    1. Patient is administered a medication.
    2. Two operations: Deducting the medication quantity from inventory and updating patient's medication history.
  - These operations must be treated as one transaction. If updating the patient's medication history fails, the deduction from the inventory must also be rolled back.

- **Outcome**: Transactions guarantee that databases remain in a consistent state even when faced with failures, errors, or system crashes.

---


### ACID Transactions

- **Atomicity**: All operations within a transaction are completed successfully; or the whole the transaction is aborted.
  
- **Consistency**: Ensures a transaction brings the database from one valid state to another.

- **Isolation**: Ensures each transaction is executed in isolation from other transactions.
  
- **Durability**: Ensures that once a transaction has been committed, it remains so, even in the face of system failures.

---

## OLAP vs OLTP

- **OLAP (Online Analytical Processing)**
  - Used for complex data analysis and queries
  - Supports decision-making processes
  - Focus on multidimensional analytical processes

- **OLTP (Online Transaction Processing)**
  - Used for managing transaction-based applications
  - Supports day-to-day operations
  - Focus on fast, routine transactions

---

## OLAPT vs OLTP Comparison

|                     | OLAP                      | OLTP                    |
|---------------------|---------------------------|-------------------------|
| **Focus**           | Business analysis         | Transaction processing  |
| **Queries**         | Complex                   | Short & fast            |
| **Size**            | Large (100s GB to TBs)    | Smaller (10s GB)        |

---


## Potential Drawbacks of Using a Relational Db

- Scalability Challenges
- Complexity in Setup and Maintenance
- Not ideal for all data models (e.g., hierarchical or graph data)

---

<!-- _class: lead -->

# Conclusion

- Relational databases offer structured and reliable storage solutions.
- Key concepts: tables, rows, columns, primary/foreign keys, normalization.
- Choose the right database based on the specific needs and data model.

