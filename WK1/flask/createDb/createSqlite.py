## check of see if the database exists: database.sqlite

import os
import sqlite3
import pandas as pd 

# check if the database exists
if os.path.exists('database.sqlite'):
    os.remove('database.sqlite')
else:
    print("The database does not exist")
    ## create the database in ./WK1/flask
    open('./WK1/flask/database.sqlite', 'w').close()

# create a connection to the database
conn = sqlite3.connect('./WK1/flask/database.sqlite')

# create a cursor object
cur = conn.cursor()

# check to see if 'costs' table exists using sqlalchemy
# if it does, drop it

cur.execute("DROP TABLE IF EXISTS costs_sbm_eastern")

# create the table using pandas
df = pd.read_csv('WK1/data/113243405_StonyBrookEasternLongIslandHospital_standardcharges.csv')

# just keep first 5 columns
df = df.iloc[:, 0:5]

# set column names: 0 is cpt, 1 is cpt_description, 2 is setting, 3 is type, and 4 is price
df.columns = ['cpt', 'cpt_description', 'setting', 'type', 'price']
df.to_sql('costs_sbm_eastern', conn, if_exists='replace', index=False)

# commit the changes
conn.commit()

# close the connection
conn.close()
