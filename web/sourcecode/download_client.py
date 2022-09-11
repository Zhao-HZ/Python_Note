import socket

def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest_ip = input("Please input the IP of the downloading server: ")
    dest_port = int(input("Please input the port of the downloading server: "))
    tcp_socket.connect((dest_ip, dest_port))
    download_file_name = input("Please input the file name: ")
    tcp_socket.send(download_file_name.encode("utf-8"))
    recv_data = tcp_socket.recv(1024 * 1024)
    with open("[FILE]" + download_file_name, 'wb') as f:
        f.write(recv_data)
    tcp_socket.close()

if __name__ == "__main__":
    main()
