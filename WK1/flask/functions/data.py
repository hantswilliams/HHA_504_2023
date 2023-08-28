## get a random sample of 10 rows from the database
import sqlite3
import pandas as pd
import sys

sys.path.append('./WK1/flask')

def dataRetrieve():

    # create a connection to the database
    conn = sqlite3.connect('database.sqlite')

    cur = conn.cursor()

    # get a random sample of 10 rows from the database
    cur.execute("SELECT * FROM costs_sbm_eastern ORDER BY RANDOM() LIMIT 100")

    # fetch the data
    data = cur.fetchall()

    # save the data to a dataframe
    df = pd.DataFrame(data)

    # keep only columns 0, 1, 2, 3, 4 in df 
    df = df.iloc[:, 0:5]

    # set column names: 0 is cpt, 1 is cpt_description, 2 is setting, 3 is type, and 4 is price
    df.columns = ['cpt', 'cpt_description', 'setting', 'type', 'price']

    # print the dataframe
    print(df)

    # close the connection
    conn.close()

    return df
