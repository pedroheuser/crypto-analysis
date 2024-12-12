import json
import pandas as pd


def analyze_data(crypto_data):
    df = pd.DataFrame(crypto_data['data'])
    df['price'] = df['quote'].apply(lambda x: x['USD']['price'] if isinstance(x, dict) else None)
    print(df[['id', 'name', 'symbol', 'price']].head())

if __name__ == "__main__":
    with open('data/cryptos_data.json', 'r') as f:
        data = json.load(f)
    analyze_data(data)
