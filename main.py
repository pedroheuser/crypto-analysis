from scripts.fetch_data import fetch_data
from scripts.process_data import process_data
from scripts.analyze_data import analyze_data


def main():
    print("Buscando dados...")
    crypto_data = fetch_data()
    if crypto_data:
        print("Processando dados...")
        process_data(crypto_data)
        print("Analisando dados...")
        analyze_data(crypto_data)

if __name__ == "__main__":
    main()