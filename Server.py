import socket #Pythons built in networking
import threading #Used to keep recieveMsg and receiveUsers active at the same time


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
def recieveMsg(msg):
    while True:
        msg = msg.recv(1024) #1024 specifies buffer size
        distributeMsg(msg)

#Sends the message to each user in chat room
def distributeMsg(msg):
    for user in users:
        user.send(msg)
    print(msg.decode('ascii'))

def receiveUsers():
    print("Started!")
    #accept users
    while True:
        #accept a new user
        user = chatRoom.accept()

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
        thread = threading.Thread(target=distributeMsg, args=(user, ))
        thread.start()

print("Staring chat room")
print("details: ", chatRoom.getsockname())

receiveUsers()
   






