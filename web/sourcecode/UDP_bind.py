from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)
local_addr = ('172.21.239.218', 7788)
# Bind a local message
udp_socket.bind(local_addr)
recv_data = udp_socket.recvfrom(1024)
print(recv_data[0].decode('utf-8'))
# print("%s : %s" % (str(recv_data[1]), recv_data[0]))
# print(recv_data)
udp_socket.close()
