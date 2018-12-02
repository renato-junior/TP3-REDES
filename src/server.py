import sys
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

def main():
    port = int(sys.argv[1])
    # netfile = str(sys.argv[2])
    # ixfile = str(sys.argv[3])
    # netixlanfile = str(sys.argv[4])

    app.run(host='127.0.0.1', port=port)



if __name__ == '__main__':
    main()