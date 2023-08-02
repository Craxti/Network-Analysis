import bitcoin
from eth_account.account import Account
from bitcoin import Base58


# Bitcoin
def get_bitcoin_address(username):
    try:
        # Генерируем приватный ключ из имени пользователя
        private_key = bitcoin.sha256(username.encode('utf-8'))
        # Получаем публичный ключ из приватного ключа
        public_key = bitcoin.privtopub(private_key)
        # Получаем адрес из публичного ключа
        address = bitcoin.pubtoaddr(public_key)
        # Проверяем, что адрес действительный (начинается с '1' или '3')
        if not Base58.is_valid(address):
            raise ValueError("Invalid Bitcoin address generated.")
    except Exception as e:
        return f"Error generating Bitcoin address for {username}: {e}"
    return address


# Ethereum
def get_ethereum_address(username):
    try:
        # Генерируем приватный ключ из имени пользователя
        private_key = Account.from_mnemonic(username).privateKey.hex()
        # Получаем адрес из приватного ключа
        address = Account.from_key(private_key).address
        # Проверяем, что адрес действительный (имеет правильную длину)
        if len(address) != 42:
            raise ValueError("Invalid Ethereum address generated.")
    except Exception as e:
        return f"Error generating Ethereum address for {username}: {e}"
    return address
