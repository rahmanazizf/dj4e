import socket

# make a phone
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# make a connection
mysock.connect(('data.pr4e.org', 80))
# send request
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# receive data
while True:
    # recieve data in UTF-8 form
    data = mysock.recv(512)
    if len(data) < 1:
        # if no data is received, then break
        break
    # convert UTF-8 to unicode (human readable)
    print(data.decode(), end='')

# close connection
mysock.close()
