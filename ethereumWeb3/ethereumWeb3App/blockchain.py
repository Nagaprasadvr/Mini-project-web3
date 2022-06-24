import brownie.project as project
from brownie import network,accounts
import brownie.project.scripts as bs

p = project.load("C:\\Users\\home\\PycharmProjects\\Web3\\Mini-project-web3\\ethereumWeb3\\ethereumWeb3App\\brownie-project")
p.load_config()
network.connect()


def deployCon():
    return bs.run("scripts/deploy.py",method_name="deploy_con")


def store(con,address,hash):
    tx:str = bs.run("scripts/deploy.py",method_name="storeIpfs",kwargs={"IpfsContract":con,"address":address,"hash":hash})
    a = ""
    for i in tx:
        if i.isalnum() and i!="m":
            a=a+i
    return a[12:]

def fetch(con,address):
    bs.run("scripts/deploy.py",method_name="fetchIpfs",kwargs={"IpfsContract":con,"address":address})
