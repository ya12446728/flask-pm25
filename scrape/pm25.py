import pandas as pd

url = 'https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=csv'

def get_pm25():
    df = pd.read_csv(url).dropna()
    col = ['Site','county','PM25']
    datas = df[col].values.tolist()

    return col,datas
