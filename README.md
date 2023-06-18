# chat_website

# Description
This project is a simple asynchronous chat website built using Django and channels. It allows users to register, log in, create rooms, and chat with other registered users. The application utilizes channels, Daphne, and asgiref to handle HTTP and WebSocket communication in an efficient and scalable manner.

# Features
User Registration: Users can create an account by providing their desired username and password. The application securely stores user credentials and allows for easy authentication during login.

User Login: Registered users can log in to their accounts using their username and password. The login process verifies the user's credentials and grants access to the application.

Room Creation: Authenticated users can create rooms where multiple registered users can gather and chat together. Each room has a unique identifier and a name chosen by the user who created it.

Real-time Chat: Users inside a room can exchange messages in real-time. The application ensures that messages are delivered to all users in the room using WebSocket communication through channels.

# Technologies Used
Django: A high-level Python web framework used for building the chat website. It provides a robust foundation for handling user authentication, database operations, and URL routing.

Channels: The Django integration layer for building asynchronous applications. It enables the use of WebSocket communication and handles background tasks efficiently.

Daphne: An HTTP and WebSocket termination server specifically designed for Django and Channels. It serves as the interface between the web server and the Django application, allowing for high-performance WebSocket handling.

asgiref: The base ASGI (Asynchronous Server Gateway Interface) library used by Channels and Daphne. It provides a consistent interface for building asynchronous web applications in Python.

# Note
This project is nothing serious, it is just made for learning purposes.
