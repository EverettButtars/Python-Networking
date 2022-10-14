import socket
import threading

#get clients handle and port
handle = input("Enter you handle: ")
port = int(input("Enter the port: "))

#IP and port
ip = '127.0.0.1'

#create socket and connect
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip, port))

def receiveMsg(t):
    while True:
        #recieve message
        message = server.recv(1024).decode('ascii')

        #Check if message requires
        if 'DISTRIBUTINGEFILE:' in message:
        #opens file for writing
            file = open(message[message.index(':'):], 'wb')

            #stores data
            data = server.recv(1024)
            while(data):
                file.write(data)
                data = server.recv(1024)
            print("Complete!")
            file.close()
        #check if message is code word to introduce yourself
        if message == 'HANDLE':
            server.send(handle.encode('ascii'))
        else:
            print(message)

def sendMsg(t):
    while True:
        #obtain msg input
        msg = input('')
        #checks to see if it is a command
        if(msg[0] == '/' ):
            #sends request
            server.send("REQUESTFILE:{}".format(msg[1:]).encode('ascii'))
            print("Asking for file") 
            
        else: 
            fmsg = '{}: {}'.format(handle, msg )
            server.send(msg.encode('ascii'))


fileEvent = threading.event()

#create threads for both sending and recieving messages
receive_thread = threading.Thread(target=receiveMsg)
write_thread = threading.Thread(target=sendMsg)
receive_thread.start()
write_thread.start()





