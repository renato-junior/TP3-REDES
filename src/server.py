import sys
import json
from flask import Flask


class Server:
    def __init__(self, netfile_name, ixfile_name, netixlanfile_name):
        # Load data from json files
        self.net_data = self.load_data_from_json(netfile_name)
        self.ix_data = self.load_data_from_json(ixfile_name)
        self.netixlan_data = self.load_data_from_json(netixlanfile_name)

    def load_data_from_json(self, filename):
        file_content = open(filename).read()
        return json.loads(file_content)
    
    def get_all_ixp(self):
        data = {}
        data["data"] = self.ix_data["data"]
        return json.dumps(data)
    
    def get_net_id_ixp(self, ix_id):
        data = {}
        ids = []
        for obj in self.netixlan_data["data"]:
            if obj["ix_id"] == ix_id:
                ids.append(obj["net_id"])
        data["data"] = list(set(ids))
        return json.dumps(data)


app = Flask(__name__)

server = Server(
    netfile_name=str(sys.argv[2]),
    ixfile_name=str(sys.argv[3]),
    netixlanfile_name=str(sys.argv[4]))

@app.route("/")
def test():
    return str(server.net_data)

@app.route("/api/ix")
def request_1():
    return str(server.get_all_ixp())

@app.route("/api/ixnets/<int:ix_id>")
def request_2(ix_id):
    return str(server.get_net_id_ixp(ix_id))



app.run(host='127.0.0.1', port=int(sys.argv[1]))
