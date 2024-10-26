import requests

# Базовый URL API CoinGecko
base_url = "https://api.coingecko.com/api/v3"

# 1. Получение текущей цены биткойна
def get_bitcoin_price():
    response = requests.get(f"{base_url}/simple/price?ids=bitcoin&vs_currencies=usd")
    if response.status_code == 200:
        data = response.json()
        print("Текущая цена Bitcoin:", data['bitcoin']['usd'], "USD")
    else:
        print("Не удалось получить цену Bitcoin")

# 2. Получение списка криптовалют
def get_crypto_list():
    response = requests.get(f"{base_url}/coins/list")
    if response.status_code == 200:
        data = response.json()
        print("Список первых 5 криптовалют:")
        for coin in data[:5]:  # Ограничимся первыми 5 криптовалютами
            print(f"ID: {coin['id']}, Название: {coin['name']}, Символ: {coin['symbol']}")
    else:
        print("Не удалось получить список криптовалют")

# 3. Получение рыночной капитализации и объема торгов по Ethereum
def get_ethereum_market_data():
    response = requests.get(f"{base_url}/coins/markets", params={
        "vs_currency": "usd",
        "ids": "ethereum"
    })
    if response.status_code == 200:
        data = response.json()[0]
        print(f"Эфириум (Ethereum):")
        print("Рыночная капитализация:", data['market_cap'], "USD")
        print("Объем торгов за 24ч:", data['total_volume'], "USD")
    else:
        print("Не удалось получить данные по Ethereum")

# Вызов функций
get_bitcoin_price()
get_crypto_list()
get_ethereum_market_data()
