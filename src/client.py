import sys
import json
import socket

CRLF = "\r\n\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8080))

request_header = b"GET /api/netname/1 HTTP/1.0\r\nHost: 127.0.0.1\r\n\r\n"
s.send(request_header)

response = ""
while True:
    recv = s.recv(1024)
    if not recv:
        break
    response += recv.decode()

response_split = response.split(CRLF)

response_body = response_split[len(response_split)-1]

print(response_body)

s.close()