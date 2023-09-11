from flask import Blueprint, render_template
import pandas as pd

main = Blueprint('data', __name__)

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA_504_2023/main/WK1/data/113243405_StonyBrookSouthamptonHospital_StandardCharges.csv')

@main.route('/data')
def index(data=df):
    data = data.sample(15)
    return render_template('data.html', data=data)