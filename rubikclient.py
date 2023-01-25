#!/usr/bin/env pybricks-micropython
# !/usr/bin/env pybricks-micropython
import socket

HOST = ""  # The server's hostname or IP address
PORT = 8080  # The port used by the server

def http_get(url):
    import socket
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo("localhost", 8080)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, "localhost"), 'utf8'))
    data = s.recv(2048).decode()
    _,_,rest = data.partition("<body>")
    result,_,_ = rest.partition("</body>")
    print (result)
    s.close()

test_string = "DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL"
http_get("http://localhost:8080/{}".format(test_string))
