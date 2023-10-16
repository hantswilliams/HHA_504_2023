import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, inspect

"""

This script uses the pymysql library for connecting to MySQL, 
so you might need to install that (pip install pymysql) if you haven't already.

It also uses python-dotenv for bringing in secrets from your .env file 

The .env should have the following in it:

DB_HOST=your_host
DB_DATABASE=your_database_name
DB_USERNAME=your_username
DB_PASSWORD=your_password
DB_PORT=3306
DB_CHARSET=utf8mb4

The default port is set to 3306 for MySQL, but you can override it by 
modifying the DB_PORT in your .env file.

The connection string is MySQL-specific, incorporating the specified port and charset.

"""

load_dotenv()  # Load environment variables from .env file

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)


####### 2nd way of creating....if need to keep on SSL mode
sql_connection_string = 'mysql+pymysql://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST + ':' + DB_PORT + '/' + DB_DATABASE # noqa 
db_engine = create_engine(sql_connection_string,
                         connect_args={'ssl': {'ssl-mode': 'preferred'}},
                         pool_size=1,
                         max_overflow=0,
                         pool_recycle=3600,
                         pool_pre_ping=True,
                         pool_use_lifo=True)

##################################################################


def get_tables(engine):
    """Get list of tables."""
    inspector = inspect(engine)
    return inspector.get_table_names()

def execute_query_to_dataframe(query: str, engine):
    """Execute SQL query and return result as a DataFrame."""
    return read_sql(query, engine)


# Example usage
tables = get_tables(db_engine)
print("Tables in the database:", tables)

sql_query = "SELECT * FROM your_table_name"  # Modify as per your table
df = execute_query_to_dataframe(sql_query, db_engine)
print(df)
