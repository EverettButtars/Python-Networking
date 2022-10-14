import socket
import threading

#get clients handle
handle = input("Enter you handle: ")

#IP and port
ip = '127.0.0.1'
port = 0

#create socket and connect
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip, port))

def receiveMsg():
    while True:
        #recieve message
        message = server.recv(1024).decode('ascii')

        #check if message is code word to introduce yourself
        if message == 'HANDLE':
            server.send(handle.encode('ascii'))
        else:
            print(message)

def sendMsg():
    while True:
        #format message and send it!
        msg = '{}: {}'.format(handle, input(''))
        server.send(msg.encode('ascii'))

#create threads for both sending and recieving messages
receive_thread = threading.Thread(target=receiveMsg)
write_thread = threading.Thread(target=sendMsg)
receive_thread.start()
write_thread.start()
