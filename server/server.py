import socket
import threading
import datetime
import configparser #config file for ip and port 

def handle_client(client_socket, client_address, client_id):
    with client_socket as sock:
        try:
            while True:
                message = sock.recv(1024).decode('utf-8')
                if not message:
                    break

                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_message = f"{timestamp} - Client{client_id} ({client_address}): {message}"
                print(log_message)
                with open("log.txt", "a") as log_file:
                    log_file.write(log_message + "\n")
                
        except ConnectionResetError:
            print(f"Connection with Client{client_id} ({client_address}) was lost.")

def run_server():
    #IP and Port
    config = configparser.ConfigParser()
    config.read('server_config.ini')  # the name of config file name
    host = config['DEFAULT']['Host']
    port = config['DEFAULT'].getint('Port')
    
    #Socket for connection 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")

    client_id = 0
    while True:
        client_socket, client_address = server.accept()
        client_id += 1
        print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address, client_id))
        thread.start()

if __name__ == "__main__":
    run_server()
