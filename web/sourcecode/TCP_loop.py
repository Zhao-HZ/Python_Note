import socket

def main():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind(("", 7890))
    tcp_server.listen(128)
    # Waiting for a client
    while True:
        print('Wait the comming for client')
        new_client_socket, client_addr = tcp_server.accept()
        print('A new client is comming %s' % str(client_addr))
        # Cycling many times and serving for the same client many times
        while True:
            recv_data = new_client_socket.recv(1024)
            print('The requests of the client is : %s' % recv_data.decode('utf-8'))
            if recv_data: 
                new_client_socket.send('OK guys!'.encode('utf-8'))
            else:
                break
        new_client_socket.close()
    tcp_server.close()
    print('Finish')

if __name__ == '__main__':
    main()
