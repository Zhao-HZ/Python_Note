import socket

message = input()
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.sendto(message.encode('utf-8'), ('172.21.224.1', 8080))
udp_socket.close()
#Send some messages until you type q
"""
while True:
    text = input()
    if text[0] == 'q':
        break
    #Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #send and receive data
    udp_socket.sendto(text.encode('utf-8'), ("172.19.0.1", 8081))
    #Close
    udp_socket.close()
""" 