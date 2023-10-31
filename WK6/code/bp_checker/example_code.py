import requests 
import pandas as pd 

df = pd.DataFrame({
    'systolic': [100, 121, 131, 140],
    'diastolic': [80, 50, 80, 75]
})

df[:1]['systolic']


analysis = requests.get(
    url = 'https://us-east1-hants-504-2023.cloudfunctions.net/bp-checker-hants',
    params = ({
        "systolic": df[:1]['systolic'],
        "diastolic": df[:1]['diastolic']
    })
)

analysis.text