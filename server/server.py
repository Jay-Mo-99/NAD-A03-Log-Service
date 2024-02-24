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
                
        except ConnectionResetError: #Connection Error with Client 
            timestamp = datetime.datetime.now().strftime(timestamp_format)
            connection_error_message = entry_format.format(timestamp=timestamp, client_id=client_id, client_address=client_address, message="Error: Connection was lost")
            print(connection_error_message)
            with open("log.txt", "a") as log_file:
                log_file.write(connection_error_message + "\n")
            pass
                           
        except socket.timeout: #Occurs when clients don't respond within a certain amount of time
            timestamp = datetime.datetime.now().strftime(timestamp_format)
            error_message = entry_format.format(timestamp=timestamp, client_id=client_id, client_address=client_address, message="Error: Client don't respond with server")
            print(error_message)
            with open("log.txt", "a") as log_file:
                log_file.write(error_message + "\n")
            pass
        
        except Exception as e:# Handle other unexpected exceptions
            timestamp = datetime.datetime.now().strftime(timestamp_format)
            generic_error_message = entry_format.format(timestamp=timestamp, client_id=client_id, client_address=client_address, message=f"Error: Unexpected error occurred - {e}")
            print(generic_error_message)
            with open("log.txt", "a") as log_file:
                log_file.write(generic_error_message + "\n")

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