import socket
import threading
import datetime
import configparser

def handle_client(client_socket, client_address, client_id, timestamp_format, entry_format):
    with client_socket as sock:
        try:
            while True:
                message = sock.recv(1024).decode('utf-8')
                if not message:
                    break

                timestamp = datetime.datetime.now().strftime(timestamp_format)
                log_message = entry_format.format(timestamp=timestamp, client_id=client_id, client_address=client_address, message=message)
                print(log_message)
                with open("log.txt", "a") as log_file:
                    log_file.write(log_message + "\n")
                
        except ConnectionResetError:
            print(f"Connection with Client{client_id} ({client_address}) was lost.")

def run_server():
    config = configparser.ConfigParser()
    config.read('server_config.ini')
    host = config['DEFAULT']['Host']
    port = config['DEFAULT'].getint('Port')
    
    timestamp_format = config['LOG_FORMAT']['TimestampFormat']
    entry_format = config['LOG_FORMAT']['EntryFormat']
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")

    client_id = 0
    while True:
        client_socket, client_address = server.accept()
        client_id += 1
        print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")
        # Pass the timestamp_format and entry_format to the handle_client function
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address, client_id, timestamp_format, entry_format))
        thread.start()

if __name__ == "__main__":
    run_server()