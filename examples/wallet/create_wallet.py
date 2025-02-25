from tonutils.client import TonapiClient
from tonutils.wallet import (
    WalletV3R1,
    # Uncomment the following lines to use different wallet versions:
    # WalletV3R2,
    # WalletV4R1,
    # WalletV4R2,
    # WalletV5R1,
    # HighloadWalletV2,
)

# API key for accessing the Tonapi (obtainable from https://tonconsole.com)
API_KEY = ""

# Set to True for test network, False for main network
IS_TESTNET = True


def main() -> None:
    # Initialize the TonapiClient
    client = TonapiClient(api_key=API_KEY, is_testnet=IS_TESTNET)

    # Create a WalletV3R1
    wallet, public_key, private_key, mnemonic = WalletV3R1.create(client)

    # Uncomment and use the following lines to create different wallet versions:
    # wallet, public_key, private_key, mnemonic = WalletV3R2.create(client)
    # wallet, public_key, private_key, mnemonic = WalletV4R1.create(client)
    # wallet, public_key, private_key, mnemonic = WalletV4R2.create(client)
    # wallet, public_key, private_key, mnemonic = WalletV5R1.create(client)
    # wallet, public_key, private_key, mnemonic = HighloadWalletV2.create(client)

    print("Wallet has been successfully created!")
    print(f"Address: {wallet.address.to_str()}")
    print(f"Mnemonic: {mnemonic}")


if __name__ == "__main__":
    main()
