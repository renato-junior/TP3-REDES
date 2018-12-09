import sys
import json
import socket

CRLF = "\r\n\r\n"
server = "127.0.0.1"
port = 8080


def get_request(server, port, path):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    request_header = bytes("GET "+str(path)+" HTTP/1.0\r\nHost: "+server+"\r\n\r\n", "UTF-8")
    s.send(request_header)
    response = ""
    while True:
        recv = s.recv(1024)
        if not recv:
            break
        response += recv.decode()
    s.close()
    response_split = response.split(CRLF)
    response_body = response_split[len(response_split)-1]
    return response_body

def get_all_ix():
    response = get_request(server, port, "/api/ix")
    return json.loads(response)

def get_ix_networks(ix_id):
    response = get_request(server, port, "/api/ixnets/{}".format(ix_id))
    return json.loads(response)

def get_network_name(net_id):
    response = get_request(server, port, "/api/netname/{}".format(net_id))
    return json.loads(response)

def analysis_0():
    net_quantities = {}
    ixs = get_all_ix()
    for ix in ixs["data"]:
        nets = get_ix_networks(ix["id"])
        for net in nets["data"]:
            if net not in net_quantities:
                net_quantities[net] = 1
            else:
                net_quantities[net] += 1
    for net in net_quantities:
        net_name = get_network_name(net)["data"]
        print("{}\t{}\t{}".format(net, net_name, net_quantities[net]))

def analysis_1():
    ixs = get_all_ix()
    for ix in ixs["data"]:
        nets = get_ix_networks(ix["id"])
        nets_count = len(nets["data"])
        print("{}\t{}\t{}".format(ix["id"], ix["name"], nets_count))

analysis_1()