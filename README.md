# Overview

To test my networking skills, I wrote a simple chatroom. The two files are the server and the client. Each file you may just simply run using python. Make sure to edit the ip and port. The client will ask you to enter your handle so other users may identify you.

I created this to better understand and test my knowledge of networking, using specifically python. Python sure makes it easy.

(you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](https://youtu.be/tYOK58aRaoE)

# Network Communication

I used a client and server model as to have multiple clients connected. I also used TCP and I used port . The format of messages sent to the server and then distributed are "(Handle of client): message. As to keep track of who is speaking.

# Development Environment

I used Python and it's socket library, it simplified a lot of the programming. I also used the built in threading library for the server and client to send and recieve messages at the same time.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [https://hackernoon.com/](https://hackernoon.com/creating-command-line-based-chat-room-using-python-oxu3u33)
- This website broke down a very simple client sever setup. I thought the use of threading for the sending and recieving so I implimented that idea.

* [dev.to](https://dev.to/black_strok3/difference-between-udp-and-tcp-example-code-1pg1)
- This helped me understand the difference between UDP and TCP and how both looked in the code. I designed my client side after this and hackernoon's models.

# Future Work

* Provide more error checking on both ends
* Remove client's own chats from log, other the that he entered
* Send files to specific people, rather then to whole chatroom
