import ethereumJSON


# Not working
class DatabaseAPI:

    def __init__(self):
        self.json = ethereumJSON.EthereumJSON()

    def put(self, db, key, value):
        self.json.sendJSONRequest("db_put", db, key, value)

    def get(self, db, key):
        self.json.sendJSONRequest("db_get", db, key)

    def putString(self, db, key, value):
        self.json.sendJSONRequest("db_putString", db, key, value)

    def getString(self, db, key):
        self.json.sendJSONRequest("db_getString", db, key)

