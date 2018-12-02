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


app = Flask(__name__)

server = Server(
    netfile_name=str(sys.argv[2]),
    ixfile_name=str(sys.argv[3]),
    netixlanfile_name=str(sys.argv[4]))

@app.route("/")
def hello():
    return str(server.net_data)

app.run(host='127.0.0.1', port=int(sys.argv[1]))
