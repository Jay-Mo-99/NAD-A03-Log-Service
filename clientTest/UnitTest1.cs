using client;
using NUnit.Framework;
using Moq;
using System.Net.Sockets;
using System;
using System.Text;

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
            mockStream = new Mock<NetworkStream>();
            mockClient = new Mock<TcpClient>();
            mainWindow = new MainWindow();

            //TcpClient and NetworkStream mock object settings
            mockClient.Setup(c => c.GetStream()).Returns(mockStream.Object);
        }

        [Test]
        public void TestSendMessageToServer()
        {
            // Arrange
            string testMessage = "Test message";
            byte[] messageBytes = Encoding.ASCII.GetBytes(testMessage);

            // Act
            mainWindow.SendMessageToServer(testMessage);

            // Assert
            mockStream.Verify(stream => stream.Write(messageBytes, 0, messageBytes.Length), Times.Once);
        }

    }
}