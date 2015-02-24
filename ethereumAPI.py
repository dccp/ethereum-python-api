import ethereumJSON

class EthereumAPI:

    def __init__(self):
        self.json = ethereumJSON.EthereumJSON()

    def coinbase(self):
        return self.json._sendJSONRequest("coinbase")

    # Not implemented 150220 in go-ethereum
    # Implemented in cpp-ethereum
    def setCoinbase(self, coinbase):
        return self._sendJSONRequest("setCoinbase", coinbase)

    def listening(self):
        return self._sendJSONRequest("listening")

    # Not implemented 150220 in go-ethereum
    # Implemented in cpp-ethereum
    def setListening(self, listening):
        return self._sendJSONRequest("setListening", listening)

    def mining(self):
        return self._sendJSONRequest("mining")

    # Not implemented 150220 in go-ethereum
    # Implemented in cpp-ethereum
    def setMining(self, mining):
        return self._sendJSONRequest("setMining", mining)

    def gasPrice(self):
        return self._sendJSONRequest("gasPrice")

    def accounts(self, client=None):
        return self._sendJSONRequest("accounts", client)

    def peerCount(self):
        return self._sendJSONRequest("peerCount")

    def defaultBlock(self):
        return self._sendJSONRequest("defaultBlock")

    def setDefaultBlock(self, block):
        return self._sendJSONRequest("setDefaultBlock", block)

    def number(self):
        return self._sendJSONRequest("number")

    def balanceAt(self, address):
        return self._sendJSONRequest("balanceAt", address)

    # Not working :( TODO:
    def stateAt(self, address, index):
        return self._sendJSONRequest("stateAt", address, index)

    def storageAt(self, address):
        return self._sendJSONRequest("storageAt", address)

    def countAt(self, address):
        return self._sendJSONRequest("countAt", address)

    def transactionCountByHash(self, hash):
        return self._sendJSONRequest("transactionCountByHash", hash)

    def transactionCountByNumber(self, number):
        return self._sendJSONRequest("transactionCountByNumber", number)

    def uncleCountByHash(self, hash):
        return self._sendJSONRequest("uncleCountByHash", hash)

    def uncleCountByNumber(self, number):
        return self._sendJSONRequest("uncleCountByNumber", number)

    def codeAt(self, address):
        return self._sendJSONRequest("codeAt", address)

    # TODO: test
    def transact(self, code):
        return self._sendJSONRequest("transact", json.dumps({"code":code}))

    # TODO: test
    def call(self, to, data):
        return self._sendJSONRequest("call", json.dumps({"to":to, "data":data}))

    def flush(self):
        return self._sendJSONRequest("flush")

    # TODO: Not working :(
    def blockByHash(self, hash):
        return self._sendJSONRequest("blockByHash", hash)

    def blockByNumber(self, number):
        return self._sendJSONRequest("blockByNumber", number)

    # TODO: test
    def transactionByHash(self, hash, index):
        return self._sendJSONRequest("transactionByHash", hash, index)

    # Exception?
    def transactionByNumber(self, number, index):
        return self._sendJSONRequest("transactionByNumber", number, index)

    # TODO: test
    def uncleByHash(self, hash, index):
        return self._sendJSONRequest("uncleByHash", hash, index)

    def uncleByNumber(self, number, index):
        return self._sendJSONRequest("uncleByNumber", number, index)

    def compilers(self):
        return self._sendJSONRequest("compilers")

    # TODO: def lll():

    def solidity(self, contract):
        return self._sendJSONRequest("solidity", contract)

    # TODO: test when implemented in ethereum
    #def serpent(contract):
    #    return self._sendJSONRequest("serpent", contract)

    # TODO: test
    def newFilter(self, topic):
        return self._sendJSONRequest("newFilter", json.dumps({"topic":topic}))

    # TODO: test
    def newFilterString(self, string):
        return self._sendJSONRequest("newFilterString", string)

    # TODO: test
    def uninstallFilter(self, id):
        return self._sendJSONRequest("uninstallFilter", id)

    def changed(self, id):
        return self._sendJSONRequest("changed", id)

    def filterLogs(self, id):
        return self._sendJSONRequest("filterLogs", id)

    def logs(self, topic):
        return self._sendJSONRequest("logs", json.dumps({"topic":topic}))

    def getWork(self):
        return self._sendJSONRequest("getWork")

    def submitWork(self, work):
        return self._sendJSONRequest("submitWork", work)

