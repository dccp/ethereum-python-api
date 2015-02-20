import json, requests

def getRPCId():
    return 1

def sendJSONRequest(method, params):
    data = json.dumps({"jsonrpc":"2.0", "method":method, "params":params, "id":getRPCId()})
    response = requests.post("http://localhost:1337", data=data)
    return response.json()['result']

def eth_coinbase():
    return sendJSONRequest("eth_coinbase", [])

def eth_setCoinbase(coinbase): # Not implemented 150220
    return sendJSONRequest("eth_setCoinbase", [coinbase])

print eth_coinbase()
