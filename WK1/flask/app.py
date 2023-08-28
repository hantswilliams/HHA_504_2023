from flask import Flask, render_template, request, redirect, url_for, flash
from functions.data import dataRetrieve
from functions.search import searchData

app = Flask(__name__)

data = dataRetrieve()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', data=data)

@app.route('/find', methods=['GET', 'POST'])
def find():
    if request.method == 'POST':
        search = request.form['search']
        searchResults = searchData(search)
        return render_template('index.html', data=searchResults)
    else:
        return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)