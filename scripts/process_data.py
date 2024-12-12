import json
import pandas as pd

def process_data(crypto_data):
    df = pd.DataFrame(crypto_data['data'])
    df.to_csv('data/cryptos_data.csv', index=False)

    print("Dados processados e salvos em cryptos_data.csv")

if __name__ == "__main__":
    with open('data/cryptos_data.json', 'r') as f:
        crypto_data = json.load(f)
    process_data(crypto_data)
