import socket

def main():
    #Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #send and receive data
    udp_socket.sendto(b'hahaha', ('10.161.1.146', ))
    #Close
    udp_socket.close()

if __name__ == '__main__':
    main()
