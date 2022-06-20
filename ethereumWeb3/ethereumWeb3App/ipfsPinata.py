import json
import ntpath
from pinatapy import *
from pinatapy import PinataPy


apiToken = "ec951faecae26fb5ef37"
apiSecret = "bbd2b47457d7076dfbd6c68d42e673bad1844a418c1f8e94d6d5662fa930ea00"

apiJwt =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI4OWEwY2JkZC0wZGM1LTQzYzctYWE3Ni02NmVjNGQ1Yjc1OGMiLCJlbWFpbCI6Im5hZ2FwcmFzYWR2cjI0NkBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicGluX3BvbGljeSI6eyJyZWdpb25zIjpbeyJpZCI6IkZSQTEiLCJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MX1dLCJ2ZXJzaW9uIjoxfSwibWZhX2VuYWJsZWQiOmZhbHNlLCJzdGF0dXMiOiJBQ1RJVkUifSwiYXV0aGVudGljYXRpb25UeXBlIjoic2NvcGVkS2V5Iiwic2NvcGVkS2V5S2V5IjoiZWM5NTFmYWVjYWUyNmZiNWVmMzciLCJzY29wZWRLZXlTZWNyZXQiOiJiYmQyYjQ3NDU3ZDcwNzZkZmJkNmM2OGQ0MmU2NzNiYWQxODQ0YTQxOGMxZjhlOTRkNmQ1NjYyZmE5MzBlYTAwIiwiaWF0IjoxNjU1NjEwNjIyfQ.wxLH6ZieDpc7aPq9JfTpUSz2SF43j1yZEVy6AM3-gQs"

def upload(filepath,filename):

    pinata = PinataPy(pinata_api_key=apiToken,pinata_secret_api_key=apiSecret)
    jsonresp = pinata.pin_file_to_ipfs(path_to_file=filepath)

    res2 = pinata.pin_list(({'status': 'pinned', 'metadata[name]': filename}))

    json_s = json.dumps(res2)
    j = json.loads(json_s)
    return j


