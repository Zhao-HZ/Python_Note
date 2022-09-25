from socket import *

tcp_client_socket = socket(AF_INET, SOCK_STREAM)
server_ip = input('Enter your IP')
server_port = int(input('Enter the port'))
#Key Step
tcp_client_socket.connect((server_ip, server_port))
send_data = input('Enter your data')

tcp_client_socket.send(send_data.encode('utf-8'))

recv_data = tcp_client_socket.recv(1024)
print("The receive data is : ", recv_data.decode('utf-8'))

tcp_client_socket.close()