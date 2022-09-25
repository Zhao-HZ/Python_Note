from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)
dest_addr = ('172.21.224.1', 8080)
send_data = input()
udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
recv_data = udp_socket.recvfrom(1024)
# print(recv_data[0].decode('utf-8'))
# print(recv_data[1])
print(recv_data)
udp_socket.close()