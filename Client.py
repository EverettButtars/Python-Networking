import socket
import threading
import os

#get clients handle and port
handle = input("Enter your handle: ")
port = int(input('port: '))

#IP and port     
ip = '127.0.0.1'

#create socket and connect
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip, port))

def receiveMsg():
    while True:
        #recieve message
        message = server.recv(1024).decode('ascii')

        #Check if message requires
        if 'DISTRIBUTINGEFILE:' in message:
        #opens file for writing
            print("start download")
            print(os.getcwd())
            file = open(message[(1+message.index(':')):], 'x')
            file = open(message[(1+message.index(':')):], 'w+b')
            #stores data
            print("file opened, receiving data")
            
            data = server.recv(1024)
            fileSize = int(data)

            total = 0
            data = server.recv(1024)
            total += len(data)
            while(data):
                file.write(data)
                if (total < fileSize):    
                    data = server.recv(1024)
                    total = total + len(data)
                else:
                    print("breaking")
                    break
                
            file.close()
            print("Complete!")
        #check if message is code word to introduce yourself
        elif message == 'HANDLE':
            server.send(handle.encode('ascii'))
        elif len(message) > 0: 
            print(message)
      

def sendMsg():
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
            server.send(fmsg.encode('ascii'))


#create threads for both sending and recieving messages
receive_thread = threading.Thread(target=receiveMsg)
write_thread = threading.Thread(target=sendMsg)
receive_thread.start()
write_thread.start()