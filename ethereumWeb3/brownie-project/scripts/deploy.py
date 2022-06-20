import os

from brownie import accounts, config


def deploy_con():
    account = accounts[0]
    print(config["wallets"]["from_key"])


def main():
    deploy_con()