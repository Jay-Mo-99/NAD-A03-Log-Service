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

namespace client
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        int port;
        string message;
        NetworkStream stream;
        byte[] sendData;
        TcpClient client;
        public MainWindow()
        {
            InitializeComponent();
        }

        //If the client click the connect button 
        private void btn_Connect_Click(object sender, RoutedEventArgs e)
        {
            //If the user input invalid input in txt_Port
            if(!int.TryParse(txt_Port.Text, out int port))
            {
                //Input Problem of Client is Notice situation
                //Add the listbox and Send Notice to Server
                listBox_Display.Items.Add("Notice: Port number is invalid: Please enter the number type(Ex: 8000)");
            }
            try
            {
                //If ip and port is valid, Connect with server
                client = new TcpClient(txt_IP.Text, port);
                listBox_Display.Items.Add("Info: Connection Succeed");
            }
            catch (System.Net.Sockets.SocketException)
            {
                //If connection have problem, It is the Error situation
                //Add the listbox and Send the Error situation to Server
                listBox_Display.Items.Add("Error: Connection Failed");

            }

        }

   
    }
}
