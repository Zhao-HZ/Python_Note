import socket

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 7890))
    tcp_server_socket.listen(128)
    new_client_socket, client_addr = tcp_server_socket.accept()
    file_name = new_client_socket.recv(1024).decode('utf-8')
    #print(recv_data)
    print("What client need to download is %s" % (str(client_addr), file_name))
    new_client_socket.send("hahahahahaha".encode("utf-8"))

    new_client_socket.close()
    tcp_server_socket.close()
    
if __name__ == "__main__":
    main()
