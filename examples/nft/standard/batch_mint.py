from pytoniq_core import Address

from tonutils.client import TonapiClient
from tonutils.nft import CollectionStandard
from tonutils.nft.content import OffchainCommonContent
from tonutils.wallet import WalletV4R2

# API key for accessing the Tonapi (obtainable from https://tonconsole.com)
API_KEY = ""

# Set to True for test network, False for main network
IS_TESTNET = True

# Mnemonic phrase used to connect the wallet
MNEMONIC: list[str] = []

# Address of the owner of the NFT collection
OWNER_ADDRESS = "UQ..."
COLLECTION_ADDRESS = "EQ..."

# Starting index for minting items
FROM_INDEX = 0

# Number of items to mint
ITEMS_COUNT = 100


async def main() -> None:
    client = TonapiClient(api_key=API_KEY, is_testnet=IS_TESTNET)
    wallet, _, _, _ = WalletV4R2.from_mnemonic(client, MNEMONIC)

    body = CollectionStandard.build_batch_mint_body(
        data=[
            (
                OffchainCommonContent(
                    uri=f"{index}.json"
                ),
                Address(OWNER_ADDRESS),
            ) for index in range(FROM_INDEX, ITEMS_COUNT)
        ],
        from_index=FROM_INDEX,
    )

    tx_hash = await wallet.transfer(
        destination=COLLECTION_ADDRESS,
        amount=ITEMS_COUNT * 0.05,
        body=body,
    )

    print(f"Successfully minted {ITEMS_COUNT} items in the collection at address: {COLLECTION_ADDRESS}.")
    print(f"Transaction hash: {tx_hash}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
