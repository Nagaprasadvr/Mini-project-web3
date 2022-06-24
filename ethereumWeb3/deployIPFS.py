from web3 import Web3
from solcx import compile_standard, install_solc
import json
from eth_account.hdaccount import HDPath,seed_from_mnemonic

abi = None
bytecode = None
ganache = "http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(ganache))
chain_id = 1337
admin_address = "0x9F7b18A0F6D25461a5F3FDD2Be2cb418022Ec63D"
admin_prvkey = "0xb11bdef9cf329ca9670d23410e41e5621a6c29b3cd18c6d6c7f579aabe17b6c1"
hdpath = HDPath("m/44'/60'/0'/0/account_index")

def compileContract():

    with open("./IpfsHash.sol", "r") as file:
        ipfsFile = file.read()

    # We add these two lines that we forgot from the video!
    print("Installing...")
    install_solc("0.8.0")

    # Solidity source code
    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {"IpfsHashContract.sol": {"content": ipfsFile}},
            "settings": {
                "outputSelection": {
                    "*": {
                        "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                    }
                }
            },
        },
        solc_version="0.8.0",
    )

    with open("compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)

    # get bytecode
    global bytecode
    bytecode = compiled_sol["contracts"]["IpfsHashContract.sol"]["IpfsHashContract"]["evm"][
        "bytecode"
    ]["object"]

    # get abi
    global abi
    abi = json.loads(compiled_sol["contracts"]["IpfsHashContract.sol"]["IpfsHashContract"]["metadata"])["output"]["abi"]


def deployContract():
    nonce = w3.eth.getTransactionCount(admin_address)
    transDeployDict = {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": admin_address,
        "nonce": nonce,
    }
    IpfsHash = w3.eth.contract(abi=abi, bytecode=bytecode)
    # Submit the transaction that deploys the contract
    transaction = IpfsHash.constructor().buildTransaction(transDeployDict)
    # Sign the transaction
    signed_txn = w3.eth.account.sign_transaction(transaction,private_key=admin_prvkey)
    print("Deploying Contract!")
    # Send it!
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    # Wait for the transaction to be mined, and get the transaction receipt
    print("Waiting for transaction to finish...")
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    IpfsHashtx = w3.eth.contract(address=tx_receipt.contractAddress,abi=abi)
    return IpfsHashtx


def StoreIpfsHash(IpfsHashCon,address:str, hash:str):
    nonce = w3.eth.getTransactionCount(address)
    transDict = {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": address,
        "nonce": nonce,

    }
    create = IpfsHashCon.functions.StoreIpfsHash(address,hash).buildTransaction(transDict)
    signTnx = w3.eth.account.sign_transaction(create)
    TnxSent = w3.eth.send_raw_transaction(signTnx.rawTransaction)
    TnxReceipt = w3.eth.wait_for_transaction_receipt(TnxSent)
    return TnxSent


def FetchIpfsHash(IpfsHashCon,address:str):
    Ipfshash = IpfsHashCon.functions.FetchIpfsHash(address).call()
    print(Ipfshash)
    return Ipfshash



