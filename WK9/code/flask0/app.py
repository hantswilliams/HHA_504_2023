import logging 
from flask import Flask 

logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/app.log",
    filemode="w",
    format='%(levelname)s - %(name)s - %(message)s'
)

app = Flask(__name__)

@app.route("/")
def index():
    try:
        logging.debug("success! index page has been accessed")
        return "Hello World!"
    except Exception as e:
        logging.error(f"an error occured! {e}")
        return "try again"
    
@app.route("/error")
def error():
    try:
        output = 1/0
        logging.debug("success! you have beaten math by diving a number by 0")
        return output
    except Exception as e:
        logging.error(f"an error occured! {e}")
        return "try again"
    
if __name__ == "__main__":
    app.run(debug=True)