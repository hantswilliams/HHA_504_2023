from flask import Flask, render_template
from dotenv import load_dotenv
from sqlalchemy import create_engine
import sentry_sdk
import os

load_dotenv()

DB_HOSTNAME = os.getenv('DB_HOSTNAME')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

print(f'DB_HOSTNAME: {DB_HOSTNAME}, DB_USERNAME: {DB_USERNAME}, DB_PASSWORD: {DB_PASSWORD}, DB_NAME: {DB_NAME}')

sentry_sdk.init(
    dsn="https://e1f283f2a39cf697473808cb4f826b35@o4504961083834368.ingest.sentry.io/4506299069825024",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

## create a route that throws an error
@app.route('/error')
def error():
    raise Exception('This is a test error for Sentry Testing')

## create a db connection error 
@app.route('/db-error')
def db_error():
    conn = create_engine(f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_NAME}')
    try:
        conn.connect()
    except Exception as e:
        raise Exception(f'Error connecting to the database: {e}')

if __name__ == '__main__':
    app.run(
        debug=True
    )