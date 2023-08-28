from flask import Flask, render_template, request, redirect, url_for, flash
from functions.data import dataRetrieve
from functions.search import searchCPTcode, searchCPTdescription

app = Flask(__name__)

data = dataRetrieve()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', data=data)

@app.route('/find-code', methods=['GET', 'POST'])
def find_code_value():
    if request.method == 'POST':
        print('Search term: ', request.form['search'])
        if request.form['search'] == '':
            flash('Please enter a search term')
            return redirect(url_for('index'))
        else:
            searchResults = searchCPTcode(request.form['search'])
            return render_template('index.html', data=searchResults)
    else:
        return redirect(url_for('index'))
    
@app.route('/find-code-description', methods=['GET', 'POST'])
def find_description_value():
    if request.method == 'POST':
        print('Search term: ', request.form['search'])
        if request.form['search'] == '':
            flash('Please enter a search term')
            return redirect(url_for('index'))
        else:
            searchResults = searchCPTdescription(request.form['search'])
            return render_template('index.html', data=searchResults)
    else:
        return redirect(url_for('index'))

    
if __name__ == '__main__':
    app.run(debug=True, port=5000)