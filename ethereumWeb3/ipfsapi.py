import ipfshttpclient as ipfs

con = ipfs.connect()
added = con.add("./instructions")
print(added)
print(con.cat(added["Hash"]))
