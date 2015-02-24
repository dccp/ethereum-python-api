import ethereumJSON

class WhisperAPI:

    def __init__(self):
        self.json = ethereumJSON.EthereumJSON()

    def newIdentity(self):
        return self.json._sendJSONRequest("shh_newIdentity")


    def haveIdentity(self, identity):
        return self.json._sendJSONRequest("shh_haveIdentity", identity)

    def changed(self, filter_id):
        return self.json._sendJSONRequest("shh_changed", filter_id)

    def post(self, from_addr, topic, payload, ttl, priority):
        return self.json._sendJSONRequest("shh_post", {"from":from_addr,
        "topic":topic, "payload":payload, "ttl":ttl, "priority":priority })

    def newFilter(self, topic): 
        return self.json._sendJSONRequest("shh_newFilter", {"topic":topic})

        # Not implemented in cpp-ethereum 150224
    def getMessages(self, filter_id):
        return self.json._sendJSONRequest("shh_getMessages", filter_id)
    
eth = WhisperAPI()
identity = eth.newIdentity()
print eth.haveIdentity(identity)
filter = eth.newFilter("0x68656c6c6f20776f726c64")
print filter
print eth.post(identity, "0x68656c6c6f20776f726c64", "0x68656c6c6f20776f726c64", 100, 100)
print eth.post(identity, "0x68656c6c6f20776f726c64", "0x68656c6c6f20776f726c64", 100, 100)
print eth.post(identity, "0x68656c6c6f20776f726c64", "0x68656c6c6f20776f726c64", 100, 100)
print eth.post(identity, "0x68656c6c6f20776f726c64", "0x68656c6c6f20776f726c64", 100, 100)
print eth.changed(filter)
print eth.getMessages(filter)
