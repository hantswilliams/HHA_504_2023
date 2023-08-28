import sqlite3
import pandas as pd
import sys

sys.path.append('./WK1/flask')

def searchCPTcode(search):

        print('Search term: ', search)

        # connect to the database
        conn = sqlite3.connect('database.sqlite')

        # search term captured
        print('Search term captured: ', search)

        cur = conn.cursor()
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

       

def searchCPTdescription(search):

        print('Search term: ', search)

        # connect to the database
        conn = sqlite3.connect('database.sqlite')

        # search term captured
        print('Search term captured: ', search)

        cur = conn.cursor()
        cur.execute("SELECT * FROM costs_sbm_eastern WHERE cpt_description LIKE ?", ('%' + search + '%',))

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