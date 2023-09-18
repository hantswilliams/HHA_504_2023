---
marp: true
title: SQLite
paginate: true
theme: default
---



# Working with SQLite

**Hants Williams, PhD, RN**

---


## Introducing SQLite

- Lightweight database engine
- Serverless, zero-configuration, transactional SQL database engine
- Ideal for embedded systems, prototyping, and local storage

---

## Why use SQLite?

- No server setup required
- Single file database: easy to backup and transfer
- Public domain: free for use for any purpose

---

## Strengths of SQLite

- Cross-platform
- Reliable and mature: used in many popular software
- Wide support: bindings in many programming languages

---

## Weaknesses of SQLite

- Not designed for high concurrency or large-scale applications
- Does not support right outer joins or full outer joins
- Limited ALTER TABLE support

---

## Data Encryption and Security

- SQLite does not encrypt data by default
- For encryption: SQLite Encryption Extension (SEE)
- Importance of following security best practices

---

## SQLite with Python

- Python’s standard library includes an SQLite module: `sqlite3`
- Simple CRUD operations
- Combines Python's ease with SQLite's simplicity

---

## Setting Up SQLite in Python

```python
import sqlite3
connection = sqlite3.connect('example.db')
cursor = connection.cursor()
```

---


### Create Table

```python
cursor.execute('''CREATE TABLE users (id INT, name TEXT)''')
```

### Insert Person

```python
cursor.execute('INSERT INTO users (id, name) VALUES (1, "Bob")')
```

### Read

```python
cursor.execute('SELECT * FROM users')
print(cursor.fetchall())
```

---

### Update

```python
cursor.execute('UPDATE users SET name = "Alice" WHERE id = 1')
```

### Read

```python
cursor.execute('SELECT * FROM users')
print(cursor.fetchall())
```

### Delete

```python
cursor.execute('DELETE FROM users WHERE id = 1')
```

---

## Next
We move on to utilizing SQLalchemy to interact with the Db


---

# Additional References 

- [Official Python Sqlite 3](https://docs.python.org/3/library/sqlite3.html)
- [Official Sqlite Website](https://www.sqlite.org/docs.html)
