import bitcoin
from eth_account.account import Account


# Bitcoin
def get_bitcoin_address(username):
    try:
        # Генерируем приватный ключ из имени пользователя
        private_key = bitcoin.sha256(username.encode('utf-8'))
        # Получаем публичный ключ из приватного ключа
        public_key = bitcoin.privtopub(private_key)
        # Получаем адрес из публичного ключа
        address = bitcoin.pubtoaddr(public_key)
    except BaseException:
        return f"Error generating Bitcoin address for {username}"
    return address


# Ethereum
def get_ethereum_address(username):
    try:
        # Генерируем приватный ключ из имени пользователя
        private_key = Account.from_mnemonic(username).privateKey.hex()
        # Получаем адрес из приватного ключа
        address = Account.from_key(private_key).address
    except BaseException:
        return f"Error generating Ethereum address for {username}"
    return address
