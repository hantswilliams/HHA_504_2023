import sqlite3
import pandas as pd
import sys

sys.path.append('./WK1/flask')

def searchData(search):

        ## connect to the database and search for CPT code
        ## if found, return the CPT code, description, setting, type, and price
        ## if not found, return a message that the CPT code was not found

        # create a connection to the database
        conn = sqlite3.connect('database.sqlite')

        # search term captured
        print('Search term captured: ', search)

        cur = conn.cursor()

        # get a random sample of 10 rows from the database
        cur.execute("SELECT * FROM costs_sbm_eastern WHERE cpt = ?", (search,))

        # fetch the data
        data = cur.fetchall()

        # print results
        print('Returned from search: ', data)

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

