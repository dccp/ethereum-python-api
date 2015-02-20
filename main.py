import json, requests

def getRPCId():
    return 1

def sendJSONRequest(method, params):
    data = json.dumps({"jsonrpc":"2.0", "method":method, "params":params, "id":getRPCId()})
    response = requests.post("http://localhost:1337", data=data)
    jsondata = response.json()
    if 'result' in jsondata:
        return jsondata['result']
    else:
        return jsondata['error']

def eth_coinbase():
    return sendJSONRequest("eth_coinbase", [])

def eth_setCoinbase(coinbase): # Not implemented 150220
    return sendJSONRequest("eth_setCoinbase", [coinbase])

def eth_listening():
    return sendJSONRequest("eth_listening", [])

def eth_setListening(listen): # Not implemented 150220
    return sendJSONRequest("eth_setListening", [listen])

def eth_mining():
    return sendJSONRequest("eth_mining", [])

#print eth_setListening(True)
print eth_mining()
