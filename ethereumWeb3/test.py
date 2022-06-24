from eth_account.hdaccount import HDPath,seed_from_mnemonic
seed = "glide action verb jewel system popular visa swim lock decide find opinion"
path = HDPath("m/44'/60'/0'/1")
privatekey = path.derive(seed.encode()).hex()
print(privatekey)