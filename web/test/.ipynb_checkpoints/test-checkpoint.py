from socket import * 

def main():
    count = 0
    for i in range(1, 5): 
        udp_socket = socket(AF_INET, SOCK_DGRAM)
        local_addr = ('172.21.239.218', 7788)
        udp_socket.bind(local_addr)
        recv = udp_socket.recvfrom(1024)
        print(recv[0].decode('utf-8'))    
    udp_socket.close()

if __name__ == '__main__':
    main()