# Chat_Talk
This is a simple chat room which uses Socket programming concepts.
This server can be set up on a local area network by choosing any on the computer to be a server node, 
and using that computer’s private IP address as the server IP address.
For example, if a local area network has a set of private IP addresses assigned ranging from 192.168.1.2 to 192.168.1.100,
then any computer from these 99 nodes can act as a server, and the remaining nodes may connect to the server node by using the server’s private IP address.
Care must be taken to choose a port that is currently not in usage. For example, port 22 is the default for ssh, and port 80 is the default for HTTP protocols.
So these two ports preferably, shouldn’t be used or reconfigured to make them free for usage.
