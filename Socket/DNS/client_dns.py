from socket import *

host = '108.61.128.46'
port = 12000

if __name__ == "__main__":
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((host, port))
        print('Connected to server')

        message = input('Enter message: ')
        s.sendall(message.encode('utf-8'))
        data = s.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")
    input()
