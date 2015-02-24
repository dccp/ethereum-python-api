import json, requests

class EthereumAPI:
    id

    def __init__(self):
        self.id = 0

    # TODO: Make smarter id generator
    def _getId(self):
        self.id += 1
        return self.id

    def _sendJSONRequest(self, method, *params):
        data = json.dumps({"jsonrpc":"2.0", "method":method, "params":params, "id":self._getId()})
        print data
        response = requests.post("http://localhost:1337", data=data)
        jsondata = response.json()
        if 'result' in jsondata:
            return jsondata['result']
        else:
            return jsondata['error']

    def eth_coinbase(self):
        return self._sendJSONRequest("eth_coinbase")

    # Not implemented 150220 in go-ethereum
    # Implemented in cpp-ethereum
    def eth_setCoinbase(self, coinbase):
        return self._sendJSONRequest("eth_setCoinbase", coinbase)

    def eth_listening(self):
        return self._sendJSONRequest("eth_listening")

    # Not implemented 150220 in go-ethereum
    # Implemented in cpp-ethereum
    def eth_setListening(self, listening):
        return self._sendJSONRequest("eth_setListening", listening)

    def eth_mining(self):
        return self._sendJSONRequest("eth_mining")

    # Not implemented 150220 in go-ethereum
    # Implemented in cpp-ethereum
    def eth_setMining(self, mining):
        return self._sendJSONRequest("eth_setMining", mining)

    def eth_gasPrice(self):
        return self._sendJSONRequest("eth_gasPrice")

    def eth_accounts(self, client=None):
        return self._sendJSONRequest("eth_accounts", client)

    def eth_peerCount(self):
        return self._sendJSONRequest("eth_peerCount")

    def eth_defaultBlock(self):
        return self._sendJSONRequest("eth_defaultBlock")

    def eth_setDefaultBlock(self, block):
        return self._sendJSONRequest("eth_setDefaultBlock", block)

    def eth_number(self):
        return self._sendJSONRequest("eth_number")

    def eth_balanceAt(self, address):
        return self._sendJSONRequest("eth_balanceAt", address)

    # Not working :( TODO:
    def eth_stateAt(self, address, index):
        return self._sendJSONRequest("eth_stateAt", address, index)

    def eth_storageAt(self, address):
        return self._sendJSONRequest("eth_storageAt", address)

    def eth_countAt(self, address):
        return self._sendJSONRequest("eth_countAt", address)

    def eth_transactionCountByHash(self, hash):
        return self._sendJSONRequest("eth_transactionCountByHash", hash)

    def eth_transactionCountByNumber(self, number):
        return self._sendJSONRequest("eth_transactionCountByNumber", number)

    def eth_uncleCountByHash(self, hash):
        return self._sendJSONRequest("eth_uncleCountByHash", hash)

    def eth_uncleCountByNumber(self, number):
        return self._sendJSONRequest("eth_uncleCountByNumber", number)

    def eth_codeAt(self, address):
        return self._sendJSONRequest("eth_codeAt", address)

    # TODO: test
    def eth_transact(self, code):
        return self._sendJSONRequest("eth_transact", json.dumps({"code":code}))

    # TODO: test
    def eth_call(self, to, data):
        return self._sendJSONRequest("eth_call", json.dumps({"to":to, "data":data}))

    def eth_flush(self):
        return self._sendJSONRequest("eth_flush")

    # TODO: Not working :(
    def eth_blockByHash(self, hash):
        return self._sendJSONRequest("eth_blockByHash", hash)

    def eth_blockByNumber(self, number):
        return self._sendJSONRequest("eth_blockByNumber", number)

    # TODO: test
    def eth_transactionByHash(self, hash, index):
        return self._sendJSONRequest("eth_transactionByHash", hash, index)

    # Exception?
    def eth_transactionByNumber(self, number, index):
        return self._sendJSONRequest("eth_transactionByNumber", number, index)

    # TODO: test
    def eth_uncleByHash(self, hash, index):
        return self._sendJSONRequest("eth_uncleByHash", hash, index)

    def eth_uncleByNumber(self, number, index):
        return self._sendJSONRequest("eth_uncleByNumber", number, index)

    def eth_compilers(self):
        return self._sendJSONRequest("eth_compilers")

    # TODO: def eth_lll():

    def eth_solidity(self, contract):
        return self._sendJSONRequest("eth_solidity", contract)

    # TODO: test when implemented in ethereum
    #def eth_serpent(contract):
    #    return self._sendJSONRequest("eth_serpent", contract)

    # TODO: test
    def eth_newFilter(self, topic):
        return self._sendJSONRequest("eth_newFilter", json.dumps({"topic":topic}))

    # TODO: test
    def eth_newFilterString(self, string):
        return self._sendJSONRequest("eth_newFilterString", string)

    # TODO: test
    def eth_uninstallFilter(self, id):
        return self._sendJSONRequest("eth_uninstallFilter", id)

    def eth_changed(self, id):
        return self._sendJSONRequest("eth_changed", id)

    def eth_filterLogs(self, id):
        return self._sendJSONRequest("eth_filterLogs", id)

    def eth_logs(self, topic):
        return self._sendJSONRequest("eth_logs", json.dumps({"topic":topic}))

    def eth_getWork(self):
        return self._sendJSONRequest("eth_getWork")

    def eth_submitWork(self, work):
        return self._sendJSONRequest("eth_submitWork", work)

