import socket
import threading
import datetime

def client_thread(conn, addr):
    print(f"Connected by {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"{timestamp} - {data.decode('utf-8')}"
            print(log_message)
            with open("server_log.txt", "a") as file:
                file.write(log_message + "\n")

def start_server():
    host = 'localhost'
    port = 8000  # Port to listen on

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=client_thread, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    start_server()
