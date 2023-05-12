from socket import *
from dns import *

host = ''
port = 12000

def to_ascii(msg):
    return str([ord(c) for c in msg]).encode('utf-8')

if __name__ == "__main__":   
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()

        print(f'Server listening on port {port}')
        
        while True:
            conn, addr = s.accept()
            print(f'Connected by {addr}')

            with conn:  # context manager to ensure exit
                while True:                
                    data = conn.recv(1024)
                    msg = data.decode('utf-8')
                    print(f"Received from {addr}: {msg}")
                    #client에서 받은 입력을 분석하여 각 행동을 구분하는 라인 제작
                    conn.sendall(to_ascii(msg))
                    break
