using client;
using NUnit.Framework;
using Moq;
using System.Net.Sockets;
using System;
using System.Text;
using System.Reflection;

/*
* FILE :        UnitTest1.cs
* PROJECT :     clientTest
* PROGRAMMER :  Jay Mo
* DATE :        2024-02-24
* DESCRIPTION : Test the function of the "client" project.
*
 */
namespace clientTest
{

    public class Tests
    {
        private Mock<NetworkStream> mockStream;
        private Mock<TcpClient> mockClient;
        private MainWindow mainWindow;
        [SetUp]
        public void Setup()
        {

        }

        //Test the DisconnectNetwork() function.
        [Test, Apartment(ApartmentState.STA)]
        public void TestDisconnectNetwork_Disconnect()
        {
            // Arrange
            mainWindow = new MainWindow();

            // Act
            bool result = mainWindow.DisconnectNetwork();

            // Assert
            Assert.IsFalse(result);
        }

    }
}