import json, requests

def getRPCId():
    return 1

def sendJSONRequest(method, *params):
    data = json.dumps({"jsonrpc":"2.0", "method":method, "params":params, "id":getRPCId()})
    response = requests.post("http://localhost:1337", data=data)
    jsondata = response.json()
    if 'result' in jsondata:
        return jsondata['result']
    else:
        return jsondata['error']

def eth_coinbase():
    return sendJSONRequest("eth_coinbase")

# Not implemented 150220 in go-ethereum
# Implemented in cpp-ethereum
def eth_setCoinbase(coinbase):
    return sendJSONRequest("eth_setCoinbase", coinbase)

def eth_listening():
    return sendJSONRequest("eth_listening")

# Not implemented 150220 in go-ethereum
# Implemented in cpp-ethereum
def eth_setListening(listening):
    return sendJSONRequest("eth_setListening", listening)

def eth_mining():
    return sendJSONRequest("eth_mining")

# Not implemented 150220 in go-ethereum
# Implemented in cpp-ethereum
def eth_setMining(mining):
    return sendJSONRequest("eth_setMining", mining)

def eth_gasPrice():
    return sendJSONRequest("eth_gasPrice")

def eth_accounts(client=None):
    return sendJSONRequest("eth_accounts", client)

def eth_peerCount():
    return sendJSONRequest("eth_peerCount")

def eth_defaultBlock():
    return sendJSONRequest("eth_defaultBlock")

def eth_setDefaultBlock(block):
    return sendJSONRequest("eth_setDefaultBlock", block)

def eth_number():
    return sendJSONRequest("eth_number")

def eth_balanceAt(address):
    return sendJSONRequest("eth_balanceAt", address)

# Not working :( TODO:
def eth_stateAt(address, index):
    return sendJSONRequest("eth_stateAt", address, index)

def eth_storageAt(address):
    return sendJSONRequest("eth_storageAt", address)

def eth_countAt(address):
    return sendJSONRequest("eth_countAt", address)

def eth_transactionCountByHash(hash):
    return sendJSONRequest("eth_transactionCountByHash", hash)

def eth_transactionCountByNumber(number):
    return sendJSONRequest("eth_transactionCountByNumber", number)

def eth_uncleCountByHash(hash):
    return sendJSONRequest("eth_uncleCountByHash", hash)

def eth_uncleCountByNumber(number):
    return sendJSONRequest("eth_uncleCountByNumber", number)

def eth_codeAt(address):
    return sendJSONRequest("eth_codeAt", address)

# TODO: test
def eth_transact(code):
    return sendJSONRequest("eth_transact", json.dumps({"code":code}))

# TODO: test
def eth_call(to, data):
    return sendJSONRequest("eth_call", json.dumps({"to":to, "data":data}))

def eth_flush():
    return sendJSONRequest("eth_flush")

# TODO: Not working :(
def eth_blockByHash(hash):
    return sendJSONRequest("eth_blockByHash", hash)

def eth_blockByNumber(number):
    return sendJSONRequest("eth_blockByNumber", number)

# TODO: test
def eth_transactionByHash(hash, index):
    return sendJSONRequest("eth_transactionByHash", hash, index)

# Exception?
def eth_transactionByNumber(number, index):
    return sendJSONRequest("eth_transactionByNumber", number, index)

# TODO: test
def eth_uncleByHash(hash, index):
    return sendJSONRequest("eth_uncleByHash", hash, index)

def eth_uncleByNumber(number, index):
    return sendJSONRequest("eth_uncleByNumber", number, index)

def eth_compilers():
    return sendJSONRequest("eth_compilers")

# TODO: def eth_lll():

def eth_solidity(contract):
    return sendJSONRequest("eth_solidity", contract)

# TODO: test when implemented in ethereum
#def eth_serpent(contract):
#    return sendJSONRequest("eth_serpent", contract)

# TODO: test
def eth_newFilter(topic):
    return sendJSONRequest("eth_newFilter", json.dumps({"topic":topic}))

# TODO: test
def eth_newFilterString(string):
    return sendJSONRequest("eth_newFilterString", string)

# TODO: test
def eth_uninstallFilter(id):
    return sendJSONRequest("eth_uninstallFilter", id)

def eth_changed(id):
    return sendJSONRequest("eth_changed", id)

def eth_filterLogs(id):
    return sendJSONRequest("eth_filterLogs", id)

