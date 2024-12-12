import json
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from config.config import url, parameters, headers

def fetch_data():
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        response.raise_for_status()
        crypto_data = response.json()
        return crypto_data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(f"Erro de conexão: {e}")
    except Exception as e:
        print(f"Erro na requisição: {e}")

if __name__ == "__main__":
    crypto_data = fetch_data()
    if crypto_data:
        print(json.dumps(crypto_data, indent=4))
    if crypto_data:
        with open('data/cryptos_data.json', 'w') as json_file:
            json.dump(crypto_data, json_file, indent=4)
