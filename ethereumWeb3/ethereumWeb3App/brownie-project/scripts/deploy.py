from brownie.network import accounts
from brownie import accounts, config, IpfsHashContract
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
def deploy_con():
    admin = accounts[0]
    IpfsContract = IpfsHashContract.deploy({"from":admin})
    print(f"Contract deployed at {IpfsContract.address}")
    return IpfsContract

chain_id = 1337
def storeIpfs(IpfsContract, address:str, hash:str)->str:
    nonce = w3.eth.getTransactionCount(str(address))
    tnx = IpfsContract.StoreIpfsHash(address,hash, {"chainId": chain_id, "nonce":nonce,"gasPrice": w3.eth.gas_price, "from": address,})
    print(str(tnx))

    return str(tnx)




def fetchIpfs(IpfsContract,address:str)->str:
    hash = IpfsContract.FetchIpfsHash(address)
    print(hash)
    return hash