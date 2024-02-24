import socket
import threading
import datetime
import configparser


#
# FILE :        server.py
# PROJECT :     server
# PROGRAMMER :  Jay Mo
# DATE :        2024-02-24
# DESCRIPTION : This is the server part of the Tcp communication. 
#               Save the contents of the success/termination/message delivery of the connection to the Client in a file called "log". 
#               The generated log file is located at "server.py ". The log file will continue to accumulate until it is manually removed. 
#               Even if somebody delete the log file, the log file will be created and recorded when the server and the client are connected.
#               If a server error with the client occurs or other exception happens, consider the situation an "Error" and record it in the log file.
#
#


    ###
    #Method: handle_client
    #Purpose: Handle communication with a client.
    #         Receive messages from the client, log them, and handle exceptions.
    #Param:
    #    client_socket (socket): The socket representing the client connection.
    #    client_address (tuple): IP address and port number.
    #    client_id (int): A identifier for the client
    #    timestamp_format (str): The format string for timestamps and log.
    #    entry_format (str): The format string for log.
    #Returns: None
    ###
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
    
    # Read the server_config.ini file to get the host and port information.
    config = configparser.ConfigParser()
    config.read('server_config.ini')
    host = config['DEFAULT']['Host']
    port = config['DEFAULT'].getint('Port')
    
    # Set the timestamp format and entry format for log messages
    timestamp_format = config['LOG_FORMAT']['TimestampFormat']
    entry_format = config['LOG_FORMAT']['EntryFormat']
    
    # Initialize sockets, bind servers to hosts and ports
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    # The server waits for the client to connect; it can accommodate up to five connection requests at the same time.
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")

    client_id = 0
    while True:
             # The server accepts the client's connection and assigns a unique ID to each client    
            client_socket, client_address = server.accept()
            client_id += 1
            print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")
            # Pass the timestamp_format and entry_format to the handle_client function
            thread = threading.Thread(target=handle_client, args=(client_socket, client_address, client_id, timestamp_format, entry_format))
            thread.start()
            
      

if __name__ == "__main__":
    run_server()