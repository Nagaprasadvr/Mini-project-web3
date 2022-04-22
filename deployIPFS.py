from web3 import Web3
from solcx import compile_standard, install_solc
import json

abi = None
bytecode = None
ganache = "http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(ganache))
chain_id = 1337
sender_prvkey = "d010b5689cd9930827f095382ef4cba427de97d318a6877ed8a3573ef16b41f8"
sender = "0x1AE44c9f7850457C4367eCc33a5f758124Bb8cb6"
hash = "QmfCU7Hm5uCDoeKcN8AenawxMCKhuyMNmq3hW9cU3jTWGk"
admin_address = "0x6d349a6fEc2c919d71F6659cD63a3c28053B9ce8"
admin_prvkey = "0x366596169205a172559de4501facc84cfff0212076044feb938424d24528f84e"
private_key = "0xd010b5689cd9930827f095382ef4cba427de97d318a6877ed8a3573ef16b41f8"
nonce = w3.eth.getTransactionCount(admin_address)
transDeployDict = {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": admin_address,
        "nonce": nonce,
    }
transDict = {
    "chainId": chain_id,
    "gasPrice": w3.eth.gas_price,
    "from": sender,
    "nonce": nonce,

}


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
            "sources": {"IpfsHash.sol": {"content": ipfsFile}},
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
    bytecode = compiled_sol["contracts"]["IpfsHash.sol"]["IpfsHashContract"]["evm"][
        "bytecode"
    ]["object"]

    # get abi
    global abi
    abi = json.loads(
        compiled_sol["contracts"]["IpfsHash.sol"]["IpfsHashContract"]["metadata"]
    )["output"]["abi"]


def deployContract():

    IpfsHash = w3.eth.contract(abi=abi, bytecode=bytecode)
    # Submit the transaction that deploys the contract
    transaction = IpfsHash.constructor().buildTransaction(transDeployDict)
    # Sign the transaction
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=admin_prvkey)
    print("Deploying Contract!")
    # Send it!
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    # Wait for the transaction to be mined, and get the transaction receipt
    print("Waiting for transaction to finish...")
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    IpfsHashtx = w3.eth.contract(address=tx_receipt.contractAddress,abi=abi)
    return IpfsHashtx


def StoreIpfsHash(address:str, hash:str):
    global nonce
    nonce = w3.eth.getTransactionCount(sender)
    global transDict
    transDict["nonce"] = nonce
    create = IpfsHashCon.functions.StoreIpfsHash(address,hash).buildTransaction(transDict)
    signTnx = w3.eth.account.sign_transaction(create,sender_prvkey)
    TnxSent = w3.eth.send_raw_transaction(signTnx.rawTransaction)
    TnxReceipt = w3.eth.wait_for_transaction_receipt(TnxSent)


def FetchIpfsHash(address):
    Ipfshash = IpfsHashCon.functions.FetchIpfsHash(address).call()
    print(Ipfshash)
    return Ipfshash

compileContract()
IpfsHashCon = deployContract()

StoreIpfsHash(sender,hash)
cid = FetchIpfsHash(sender)


url: str = "https://ipfs.io/ipfs/"+cid
print(url)
