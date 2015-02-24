import ethereumJSON

class WhisperAPI:

    def __init__(self):
        self.json = ethereumJSON.EthereumJSON()

    def newIdentity(self):
        return self.json.sendJSONRequest("shh_newIdentity")

    def haveIdentity(self, identity):
        return self.json.sendJSONRequest("shh_haveIdentity", identity)

    def changed(self, filter_id):
        return self.json.sendJSONRequest("shh_changed", filter_id)

    def post(self, from_addr, topic, payload, ttl, priority):
        return self.json.sendJSONRequest("shh_post", {"from":from_addr,
        "topic":topic, "payload":payload, "ttl":ttl, "priority":priority })

    def newFilter(self, topic):
        return self.json.sendJSONRequest("shh_newFilter", {"topic":topic})

    def uninstallFilter(self, filter_id):
    	return self.json.sendJSONRequest("shh_uninstallFilter", filter_id)

        # Not implemented in cpp-ethereum 150224
    def getMessages(self, filter_id):
        return self.json.sendJSONRequest("shh_getMessages", filter_id)

