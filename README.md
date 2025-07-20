# TCP/IP Client-Server Logging Simulator

This project demonstrates a simple client-server communication using TCP/IP, along with a basic logging mechanism based on log severity levels.

## 🔀 Branch Structure

- **`main`**: Contains the **client-side** code.
- **`master`**: Contains the **server-side** code.

---

## 💻 Client Main Functions

### 🔌 Connect

- Users can connect to the server by entering the **IP** and **Port**, then clicking the **Connect** button.
- If invalid values are entered, a **message box** displays a warning.
- On a successful connection:
  - The **Connect** button is disabled.
  - The **Disconnect** button becomes active.

### 📤 Send

- After a successful connection, users can type a message and press **Send** to transmit it to the server.
- If the Send button is clicked without any input, a **warning** is shown.

### 🔌 Disconnect

- Pressing **Disconnect**:
  - Terminates the connection with the server.
  - Clears the message input field and listbox.
  - Reactivates the **Connect** button.

---

## 🪵 Log Severity Levels

### 🔴 Critical

- If a user sends **more than 20 messages** after connecting, the system flags them as an intruder.
- A warning message is displayed, and the client is **forcefully shut down**.
- The server logs this as a **Critical Issue**.

### 🟠 Error

- Triggered by network issues between the client and server.
- If the error originates from the **Client**:
  - Users can view the error via the **Listbox**.
- If the error originates from the **Server**:
  - It is recorded in the server's **log** file as an **Error**.

### 🔵 Info

- Normal events such as:
  - Connection success
  - Message sent
  - Disconnection
- These are shown in the **Listbox** and logged by the server as **Information**.

### 🟡 Notice

- Occurs when the client enters an invalid IP or port.
- The user is notified via a **message box** or the **Listbox**.
- This is **not logged** on the server.

---

## 📌 Note

- The simulator is designed to demonstrate logging, error handling, and connection management in a simple TCP/IP environment.
