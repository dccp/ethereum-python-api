import json, requests

class EthereumJSON:

    def __init__(self):
        self.id = 0

    def _getId(self):
        self.id += 1
        return self.id

    def _sendJSONRequest(self, method, *params):
        data = json.dumps({"jsonrpc":"2.0", "method":method, "params":params, "id":self._getId()})
        response = requests.post("http://localhost:1337", data=data)
        jsondata = response.json()
        if 'result' in jsondata:
            return jsondata['result']
        else:
            return jsondata['error']
