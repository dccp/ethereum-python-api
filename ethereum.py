import ethereumJSON

class EthereumAPI:

    def __init__(self):
        self.json = ethereumJSON.EthereumJSON()

    def coinbase(self):
        return self.json.sendJSONRequest("eth_coinbase")

    # Not implemented 150220 in go-ethereum
    # Implemented in cpp-ethereum
    def setCoinbase(self, coinbase):
        return self.json.sendJSONRequest("eth_setCoinbase", coinbase)

    def listening(self):
        return self.json.sendJSONRequest("eth_listening")

    # Not implemented 150220 in go-ethereum
    # Implemented in cpp-ethereum
    def setListening(self, listening):
        return self.json.sendJSONRequest("eth_setListening", listening)

    def mining(self):
        return self.json.sendJSONRequest("eth_mining")

    # Not implemented 150220 in go-ethereum
    # Implemented in cpp-ethereum
    def setMining(self, mining):
        return self.json.sendJSONRequest("eth_setMining", mining)

    def gasPrice(self):
        return self.json.sendJSONRequest("eth_gasPrice")

    def accounts(self, client=None):
        return self.json.sendJSONRequest("eth_accounts", client)

    def peerCount(self):
        return self.json.sendJSONRequest("eth_peerCount")

    def defaultBlock(self):
        return self.json.sendJSONRequest("eth_defaultBlock")

    def setDefaultBlock(self, block):
        return self.json.sendJSONRequest("eth_setDefaultBlock", block)

    def number(self):
        return self.json.sendJSONRequest("eth_number")

    def balanceAt(self, address):
        return self.json.sendJSONRequest("eth_balanceAt", address)

    # Not working :( TODO:
    def stateAt(self, address, index):
        return self.json.sendJSONRequest("eth_stateAt", address, index)

    def storageAt(self, address):
        return self.json.sendJSONRequest("eth_storageAt", address)

    def countAt(self, address):
        return self.json.sendJSONRequest("eth_countAt", address)

    def transactionCountByHash(self, hash):
        return self.json.sendJSONRequest("eth_transactionCountByHash", hash)

    def transactionCountByNumber(self, number):
        return self.json.sendJSONRequest("eth_transactionCountByNumber", number)

    def uncleCountByHash(self, hash):
        return self.json.sendJSONRequest("eth_uncleCountByHash", hash)

    def uncleCountByNumber(self, number):
        return self.json.sendJSONRequest("eth_uncleCountByNumber", number)

    def codeAt(self, address):
        return self.json.sendJSONRequest("eth_codeAt", address)

    # TODO: test
    def transact(self, code):
        return self.json.sendJSONRequest("eth_transact", json.dumps({"code":code}))

    # TODO: test
    def call(self, to, data):
        return self.json.sendJSONRequest("eth_call", json.dumps({"to":to, "data":data}))

    def flush(self):
        return self.json.sendJSONRequest("eth_flush")

    # TODO: Not working :(
    def blockByHash(self, hash):
        return self.json.sendJSONRequest("eth_blockByHash", hash)

    def blockByNumber(self, number):
        return self.json.sendJSONRequest("eth_blockByNumber", number)

    # TODO: test
    def transactionByHash(self, hash, index):
        return self.json.sendJSONRequest("eth_transactionByHash", hash, index)

    # Exception?
    def transactionByNumber(self, number, index):
        return self.json.sendJSONRequest("eth_transactionByNumber", number, index)

    # TODO: test
    def uncleByHash(self, hash, index):
        return self.json.sendJSONRequest("eth_uncleByHash", hash, index)

    def uncleByNumber(self, number, index):
        return self.json.sendJSONRequest("eth_uncleByNumber", number, index)

    def compilers(self):
        return self.json.sendJSONRequest("eth_compilers")

    # TODO: def lll():

    def solidity(self, contract):
        return self.json.sendJSONRequest("eth_solidity", contract)

    # TODO: test when implemented in ethereum
    #def serpent(contract):
    #    return self.json.sendJSONRequest("eth_serpent", contract)

    # TODO: test
    def newFilter(self, topic):
        return self.json.sendJSONRequest("eth_newFilter", json.dumps({"topic":topic}))

    # TODO: test
    def newFilterString(self, string):
        return self.json.sendJSONRequest("eth_newFilterString", string)

    # TODO: test
    def uninstallFilter(self, id):
        return self.json.sendJSONRequest("eth_uninstallFilter", id)

    def changed(self, id):
        return self.json.sendJSONRequest("eth_changed", id)

    def filterLogs(self, id):
        return self.json.sendJSONRequest("eth_filterLogs", id)

    def logs(self, topic):
        return self.json.sendJSONRequest("eth_logs", json.dumps({"topic":topic}))

    def getWork(self):
        return self.json.sendJSONRequest("eth_getWork")

    def submitWork(self, work):
        return self.json.sendJSONRequest("eth_submitWork", work)

