import socket #Pythons built in networking
import threading #Used to keep recieveMsg and receiveUsers active at the same time
import os
import time

#Create global variables

#Create the socket and variable.    
# #SOCK_STREAM = TCP
chatRoom = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#IP and port
ip = '127.0.0.1'
port = 0
#Bind everything
chatRoom.bind((ip,port))
chatRoom.listen()

#create lists for users and corresponding handles
users = []
handles = []

#Recieves message from clients
def recieveMsg(user):
    while True:

        msg = user.recv(1024).decode('ascii') #1024 specifies buffer size

        #checks if recieved file request
        if "REQUESTFILE:" in msg:
            #obtains file name from request
            fileName = msg[(msg.index(':')+1):]

            #lets everyone know they are recieving a file
            distributeMsg("DISTRIBUTINGEFILE:{}".format(fileName).encode('ascii'))

            #opens and reads file and sends it via distrubuteMsg
            file = open(fileName, 'rb')
            print("Opened")
            distributeMsg(str(int(os.path.getsize(fileName))).encode())
            time.sleep(.1)
            data = file.read(1024)
            print("Reading")
            while(data):
                distributeMsg(data)
                data = file.read(1024)
            
            
            file.close()
            print("Finished sending", fileName)

        else:
            distributeMsg(msg.encode('ascii'))
            print(msg)


#Sends the message to each user in chat room
def distributeMsg(msg):
    for user in users:
        user.send(msg)
    

def receiveUsers():
    print("Started!")
    #accept users
    while True:
        #accept a new user
        user, addy = chatRoom.accept()

        #ask for their chat handle
        user.send('HANDLE'.encode('ascii'))
        handle = user.recv(1024).decode('ascii')\
        
        #add new user to lists
        users.append(user)
        handles.append(handle)

        #announce new person has joined!
        user.send("connected!".encode('ascii'))
        distributeMsg("user {} has Joined!".format(handle).encode('ascii'))
        print("user {} has Joined!".format(handle))

        #creates a thread for distributeMsg to run
        thread = threading.Thread(target=recieveMsg, args=(user, ))
        thread.start()

print("Staring chat room")

print("details: ", chatRoom.getsockname())

receiveUsers()
   






