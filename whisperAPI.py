import ethereumJSON

class WhisperAPI:

    def __init__(self):
        self.json = ethereumJSON.EthereumJSON()

    def newIdentity(self):
        return self.json._sendJSONRequest("shh_newIdentity")


    def haveIdentity(self, identity):
        return self.json._sendJSONRequest("shh_haveIdentity", identity)

    def changed(self, number):
        return self.json._sendJSONRequest("shh_changed", number)

eth = WhisperAPI()
e = eth.newIdentity()
print eth.haveIdentity(e)
print eth.changed(7)
