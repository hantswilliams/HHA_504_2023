# Example to go off of for class 

import pandas as pd 
import numpy as np
import sqlite3
from sqlalchemy import create_engine


###### Step 1 - Extract (E) and Transform (T) ########
###### Step 1 - Extract (E) and Transform (T) ########
###### Step 1 - Extract (E) and Transform (T) ########
###### Step 1 - Extract (E) and Transform (T) ########


# Load in csv data from WK3/data/stonybrook/stonybrook.csv

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA_504_2023/main/WK3/data/stonybrook/stonybrook.csv')

# Shape
df.shape

# Columns
df.columns

## Create new column that goes from wide to long, where we keep columns 0:8 and then melt the rest into a new
## column called 'insurance_type'

columnNames = list(df)
idVars = columnNames[:8]
valueVars = columnNames[8:]

stonybrook_modified = df.melt(id_vars=idVars, value_vars=valueVars)

stonybrook_modified.columns

stonybrook_modified.rename(columns={'HospCode':'hospital_name', 
            'variable':'insurance_type', 
            'Code':'code', 
            'Description':'code_description',
             'value':'cost_negotiated', 
             'Minimum Negotiated Charge':'cost_minimum',
             'Maximum Negotiated Charge': 'cost_maximum'}, inplace=True)

stonybrook_modified['insurance_type'].value_counts()


##### Step 2 - (L) Load ########
##### Step 2 - (L) Load ########
##### Step 2 - (L) Load ########
##### Step 2 - (L) Load ########

## Create a new blank database using sqlite3

conn = sqlite3.connect('costs.db')
c = conn.cursor()

## Create a new table called 'stonybrook' and load in the data from stonybrook_modified
## manually create the schema based on the data types in stonybrook_modified

c.execute('''CREATE TABLE stonybrook
                (
                    [hospital_name] text, 
                    [insurance_type] text, 
                    [code] text, 
                    [code_description] text, 
                    [cost_negotiated] real, 
                    [cost_minimum] real, 
                    [cost_maximum] real
                )''')

conn.commit()

## Now print out the table names from the database to make sure it worked

c.execute('''SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;''')

for value in c.fetchall():
    print(value)

## Now perform a Select * on the table to make sure it worked and it returns no values

c.execute('''SELECT * FROM stonybrook''')
print(c.fetchall())

## Now perform the same query in pandas to make sure it worked

pd.read_sql('''SELECT * FROM stonybrook''', conn)

## Now using pandas, load in the data from stonybrook_modified into the table 'stonybrook'

stonybrook_modified.to_sql('stonybrook', conn, if_exists='replace', index=False)

## Now perform the same query in pandas to make sure it worked, just return the first 5 rows

pd.read_sql('''SELECT * FROM stonybrook LIMIT 5''', conn)
