from flask import Flask 
import sentry_sdk

sentry_sdk.init(
    dsn="",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/error')
def creating_error():
    try:
        1/0
    except Exception as e:
        raise Exception (f'Something went wrong: {e}')

if __name__ == "__main__":
    app.run(debug=True)