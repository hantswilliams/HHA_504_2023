from flask import Blueprint, render_template

main = Blueprint('about', __name__)

@main.route('/about')
def index():
    return render_template('about.html')