using client;
using NUnit.Framework;
using Moq;
using System.Net.Sockets;
using System;
using System.Text;
using System.Reflection;

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

        [Test, Apartment(ApartmentState.STA)]
        public void TestDisconnectNetwork()
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