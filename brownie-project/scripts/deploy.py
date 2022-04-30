from brownie import accounts, config, IpfsHashContract


def deploy():
    account = accounts.add(config["wallets"]["key1"])
    IpfsHashContract.deploy({"from":account})
    print(account)


def main():
    deploy()
