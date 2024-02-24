The "main" branch has the client's code uploaded.
The "master" branch has the server's code uploaded.

* Main Function of Client: 
*   * Connect: 
*             The user can connect to the server by entering the server's ip and port correctly and pressing the connect button. 
*             If the user enters invalid values for the ip and port, a message box will display a warning. If Connect succeeds, the Connect button will be disabled until you press Disconnect.
*
*   * Send: 
*             After a successful connection between the client and the server, users can enter a message and press the Send button to send a message to the server. 
*             If you press the Send button without entering a message, the message box displays a warning.
*
*   * Disconnect: 
*             Pressing the button removes the connection between the client and the server. 
*             Pressing the Disconnect button will reset the message entry box and listbox. At the same time, the Connect button will be reactivated.
*             
* 
* Log Severity Level:
*     * Critical:
*               If a user sends a message more than 20 times after Connect is successful, the user is recognized as an intruder. 
*               Show a warning to the user in a message box and force the client to shut down.
*               Server writes Critical Issue in the "log"
*               
*     * Error:
*               This is considered an error situation when a network error occurs between the Client and the Server. 
*               If the Error ocuured from Client, Users can query Listbox for the error.
*               If the Error occured from Server, The server writes the corresponding error in the "log". 
*               
*     * Info(Information):
*               Connection Success/Terminate/Send Message is considered normal and is displayed at the Information level. 
*               Users can look up their Info in Listbox and Server writes Info in the "log"
*               
*     * Notice:
*               The client's IP/Port input error is a notice situation that only appears to the client. 
*               Users can notify the user of the situation with a message box or query the Listbox.
*               Server doesn't write Notice Issue in the "log"
