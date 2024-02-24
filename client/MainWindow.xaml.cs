using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

/*
* FILE :        MainWindow.xaml.cs
* PROJECT :     client
* PROGRAMMER :  Jay Mo
* DATE :        2024-02-24
* DESCRIPTION :
* It includes a function of creating or deleting a log file with a specific name on the desktop and writing the contents in the log file.
* 
*  
 */
namespace client

{ 

    public partial class MainWindow : Window
    {
        int port;
        string message;
        NetworkStream stream;
        int byteCount;
        byte[] sendData;
        TcpClient client;
        private readonly object streamLock = new object(); //Lock object for Stream synchronization
        private int sendCount = 0; //Variable that track the number of message transmissions
        private const int sendLimitCount = 20; // Limit time for send 
        public bool checkDisconnet = false;



        public MainWindow()
        {
            InitializeComponent();
        }
        //Send Message to Server 
        public void SendMessageToServer(string message)
        {
            if (sendCount > sendLimitCount)
            {
                //If sendCount exceeds sendLimitCount, stop sending messages.
                return;
            }

            try
            {
                lock (streamLock) //Stream Synchronization
                {
                    byte[] data = Encoding.ASCII.GetBytes(message);
                    stream = client.GetStream();
                    stream.Write(data, 0, data.Length);
                    sendCount++; // Increase the count when sending a message

                    if (sendCount > sendLimitCount)
                    {
                        // Send warning message when sendLimitCount is exceeded
                        string warningMessage = "Critical: Client exceeded send limit";
                        listBox_Display.Items.Add("Critical: Client exceeded send limit");
                        byte[] warningData = Encoding.ASCII.GetBytes(warningMessage);
                        stream.Write(warningData, 0, warningData.Length);

                        // A message box notifies the user of the excess contact towards the server and informs the client of the forced shutdown.
                        MessageBox.Show(warningMessage +"\n"+ "This client will be forced to shut down.","Critical");

                        // Disconnect the client and close the form

                        Dispatcher.Invoke(() =>
                        {
                            btn_Disconnect_Click(this, null);
                            this.Close(); // Close the client form
                        });
                        return;
                    }
                }
            }
            catch (Exception ex)
            {
                listBox_Display.Items.Add("Error: Unable to send message to server. " + ex.Message);
            }
        }

        //If the client click the connect button 
        private void btn_Connect_Click(object sender, RoutedEventArgs e)
        {
            //If the client click the connect button, Disable until you press the Connect button
            btn_Connect.IsEnabled = false;
            btn_Disconnect.IsEnabled = true;

            //If the user input invalid input in txt_Port
            if (!int.TryParse(txt_Port.Text, out port))
            {
                //Input Problem of Client is Notice situation
                //Add the listbox and Send Notice to Server

                // A message box notifies the user of the excess contact towards the server and informs the client of the forced shutdown.
                MessageBox.Show("The IP and port you entered do not match the server", "Notice");
                listBox_Display.Items.Add("Notice: Port number is invalid: Please enter the number type(Ex: 8000)");

            }
            try
            {
                //If ip and port is valid, Connect with server
                client = new TcpClient(txt_IP.Text, port);
                listBox_Display.Items.Add("Info: Connection Succeed");
                SendMessageToServer("Info: Connection Succeed");
            }
            catch (Exception ex)
            {
                //A problem with IP and the server cannot connect is a client's input problem.Notice
                //Creating a Message Box
                MessageBox.Show(ex + "\n" + "Please check the ip and Port", "Notice");
                listBox_Display.Items.Add("Notice: Connection Failed. Please check the ip and Port");                //Add the listbox

            }

        }

        
        private void btn_Send_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                //Send the Data for server
                message = txt_Msg.Text;
                if (string.IsNullOrEmpty(message)) //Check the message is null or not
                {
                    // If there is no message, display a warning message
                    MessageBox.Show("Enter a message to send to the server and press the Send button.", "Notice");
                    return; // Return to stop running the method afterwards
                }
                SendMessageToServer("Info: Sent Data :" + message);
                listBox_Display.Items.Add("Info: Sent Data :" + message);


            }
            //If the connection is not well about sending message, It is Error. 
            catch (System.NullReferenceException ex)
            {
                listBox_Display.Items.Add("Error: Failed to sent data");
                SendMessageToServer("Error: Failed to sent data :" + ex.Message);
            }
        }

        public bool DisconnectNetwork()
        {
            lock (streamLock)
            {
                if (stream != null)
                {
                    SendMessageToServer("Info: Connection terminated");
                    stream.Close();
                    stream = null;
                    checkDisconnet = true;
                }

                if (client != null)
                {
                    client.Close();
                    client = null;
                    checkDisconnet = false;
                }

                return checkDisconnet;
            }
        }

        private void btn_Disconnect_Click(object sender, RoutedEventArgs e)
        {
            DisconnectNetwork();


            //UI Thread
            Dispatcher.Invoke(() =>
            {
                listBox_Display.Items.Add("Info: Connection terminated");

                // Re-enable the Connect button when user click Disconnect button
                btn_Connect.IsEnabled = true;
                btn_Disconnect.IsEnabled = false;

                //Initialize txt_Msg and listBox_Display
                txt_Msg.Clear();
                listBox_Display.Items.Clear();
            });
        }
    }
}
