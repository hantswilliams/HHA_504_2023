---
marp: true
theme: default
paginate: true
---

<!-- _class: lead -->

# Practicing SQL in Python: SQLite & SQLAlchemy
**Hants Williams, PhD, RN**

---

## SQLite in Python

- **SQLite**: Lightweight, file-based relational database.
- Directly integrated into Python via the `sqlite3` library.
- Perfect for prototyping and small projects.

Example:

```python
import sqlite3

conn = sqlite3.connect('healthcare.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE patients (
                  id INTEGER PRIMARY KEY,
                  first_name TEXT,
                  last_name TEXT,
                  diagnosis TEXT
                  )""")
conn.close()
```

---

## SQLAlchemy

- A popular SQL toolkit.
- Connects to various databases, including SQLite.
- Allows for both high-level ORM operations and raw SQL queries.

---

## SQLAlchemy: Versatile Database Connections

- **Multiple Databases**: SQLAlchemy isn't limited to SQLite. It can connect to various databases, including those hosted on cloud platforms like Azure and GCP.

- **Uniform Connection**: Regardless of the database backend, the connection is established using a consistent approach — the `create_engine` method with a connection string.

- **Connection Strings**:
  - SQLite: `'sqlite:///mydatabase.db'`
  - MySQL (for example on GCP): `'mysql+mysqldb://user:password@host:port/dbname'`

- **Securing Connection Strings**: 
  - For security, store connection strings in a `.env` file.



---

## Setting Up SQLAlchemy

To set up SQLAlchemy:

```bash
pip install sqlalchemy
```

Then, in Python:

```python
from sqlalchemy import create_engine

engine = create_engine('sqlite:///healthcare.db')
```

---

## Using Raw SQL with SQLAlchemy

You can execute raw SQL directly:

```python
result = engine.execute("INSERT INTO patients (first_name, last_name, diagnosis) VALUES ('Jane', 'Doe', 'Cold')")
```

---

## Querying with Raw SQL

You can retrieve data using raw SQL as well:

```python
result = engine.execute("SELECT first_name, last_name FROM patients WHERE diagnosis='Cold'")

for row in result:
    print(row.first_name, row.last_name)
```


---

## Integrating SQLAlchemy with Pandas

Once we have defined our engine using sqlalchemy, we can then even utilize that connection within pandas: 

```python
import pandas as pd

sql = "SELECT first_name, last_name, diagnosis FROM patients"
df = pd.read_sql(sql, engine)

print(df.head())
```

---

## Pushing a CSV to SQLite with Pandas & SQLAlchemy

When working with data, it's common to start with a `.CSV` file. Using Pandas and SQLAlchemy, you can easily push this data to an SQLite database.

### Steps:

1. **Load the CSV into a DataFrame**:
   ```python
   import pandas as pd

   df = pd.read_csv('data.csv')
   ```
---

2. **Push the DataFrame to SQLite**:
   ```python
   from sqlalchemy import create_engine

   engine = create_engine('sqlite:///database.db')
   df.to_sql('table_name', engine, if_exists='replace', index=False)
   ```

---

**Benefits of SQLalchemy + Pandas**:

For quickly writing to tables:
  - **Automated Schema Inference**: No need to define column names/types. Pandas infers it from the DataFrame.
  - **Flexibility**: Easily overwrite existing tables or append data with the `if_exists` parameter.
  - **Efficiency**: Push large datasets quickly without manual SQL scripting.

---

**Benefits of SQLalchemy + Pandas Continued**:

- **Ease of Use**: Convert SQL results directly into a data structure familiar to data scientists and analysts.
- **Analysis**: Leverage Pandas functionalities for data cleaning, exploration, and visualization.
- **Integration**: Seamlessly combine the strengths of SQL databases with powerful Python data tools.

---

## Benefits of SQLAlchemy with Raw SQL

1. **Flexibility**: Combines the power of raw SQL with the convenience of an ORM.
2. **Consistency**: Use the same toolkit, whether you're writing ORM-based or raw SQL queries.
3. **Connection Management**: Handles database connections, pooling, and transactions for you.

---

<!-- _class: lead -->

# Overall:

- SQLite provides a straightforward database experience for Python developers.
- SQLAlchemy offers flexibility for both ORM-based operations and raw SQL queries.
- This combination allows you to manage data efficiently in Python, irrespective of your SQL preference.

---

# Additional References 

- [Official Site](https://www.sqlalchemy.org/)
- [Official Documentation](https://docs.sqlalchemy.org/en/20/)