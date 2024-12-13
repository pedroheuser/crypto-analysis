import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_data(crypto_data):
    df = pd.DataFrame(crypto_data['data'])
    prices = df[['name', 'symbol', 'quote']].copy()
    prices['price'] = prices['quote'].apply(lambda x: x['USD']['price'])
    sns.barplot(x='symbol', y='price', data=prices.nlargest(10, 'price'))
    plt.title('Top 10 Criptomoedas por preço')
    plt.xlabel('Criptomoeda')
    plt.ylabel('Preço (USD)')
    plt.show()
    df['daily_return'] = df['quote'].apply(lambda x: x['USD']['percent_change_24h'])
    print(f"Média de retorno diário: {df['daily_return'].mean():.2f}%")


    df['price'] = df['quote'].apply(lambda x: x['USD']['price'] if isinstance(x, dict) else None)
    print(df[['id', 'name', 'symbol', 'price']].head())

if __name__ == "__main__":
    with open('data/cryptos_data.json', 'r') as f:
        data = json.load(f)
    analyze_data(data)
