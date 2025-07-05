
# Authentication Domain 🔐

## Overview 🌟

The **Authentication Domain** is a collection of microservices designed to manage user authentication and registration. This domain includes three main microservices:
- **LoginRoot**: A service that allows root users to log in.
- **Login**: A service that facilitates logging in for normal users.
- **Register**: A service that enables users to register their accounts.

All services are connected to a **SQL Server** database, which is used to store user data and credentials securely.

### Purpose 💡

The **Authentication Domain** provides a modular and scalable solution for managing user authentication. The domain's services are designed to work together while maintaining separation of concerns, allowing for easier maintenance and expansion. The system ensures that both root and normal users can log in securely, and it also provides a registration service to handle new user accounts.

## Key Features 🔑

- **LoginRoot Service**: Designed for root users, allowing them to log into the system with their credentials. This service manages authentication for administrative users.
- **Login Service**: Manages authentication for normal users, validating their credentials before granting access to the system.
- **Register Service**: Provides a registration endpoint that allows new users to create an account in the system.
- **SQL Server Integration**: All services are connected to a SQL Server database where user data, credentials, and session information are securely stored.
- **Secure Authentication**: Passwords are stored securely using encryption methods to protect user data from unauthorized access.

## Technology Stack ⚙️

- **Programming Languages**: The services are built using **Node.js** and **Express** for handling HTTP requests and responses.
- **Database**: The system uses **SQL Server** to store user data and credentials.
- **Docker**: Each service is containerized using Docker for consistent and scalable deployment.
- **Docker Compose**: The system can be deployed using **Docker Compose**, which simplifies running multiple services together.

## Folder Structure 📁

### Main Folders:
- **LoginRoot**: Contains the service responsible for logging in root users. It manages the authentication process for admin users.
- **Login**: Contains the service for logging in normal users, ensuring secure access to the system for regular users.
- **Register**: Contains the service that handles the user registration process, enabling new users to create accounts.
- **config**: Holds configuration files for environment variables and settings for each service.
- **controllers**: Contains the logic for handling HTTP requests related to user authentication and registration.
- **services**: Contains the core business logic for user login and registration.
- **utils**: Contains utility files, such as helper functions for password hashing or other security measures.
- **docker-compose.yml**: A Docker Compose configuration file that defines how all services are connected and run in containers.
- **README.md**: This file, providing an overview of the **Authentication Domain** and how it works.

## How to Deploy 🛠️

### Steps to Deploy:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Loony213/Authentication-Domain.git
    cd Authentication-Domain
    ```

2. **Build and Run with Docker Compose**:
    ```bash
    docker-compose up --build
    ```

    This command will start all the services defined in the **docker-compose.yml** file, ensuring they are correctly linked together and ready to handle requests.

3. **Access the Services**:
    After deploying, the services will be available at:
    - **LoginRoot**: Accessible at **http://localhost:8001** (or the respective service port).
    - **Login**: Accessible at **http://localhost:8002**.
    - **Register**: Accessible at **http://localhost:8003**.

---

## Technologies Used ⚙️

- **Node.js**: A JavaScript runtime used to build fast, scalable network applications.
- **Express.js**: A minimal and flexible Node.js web application framework used to handle HTTP requests.
- **SQL Server**: A relational database management system used to store user credentials and data securely.
- **Docker**: A platform for developing, shipping, and running applications in containers.
- **Docker Compose**: A tool for defining and running multi-container Docker applications.

---

### In Summary 📝

The **Authentication Domain** provides three essential microservices: **LoginRoot**, **Login**, and **Register**, which are designed to manage authentication and registration for users and admins. By utilizing **SQL Server** for storing user credentials and Docker for deployment, this domain ensures a scalable, secure, and easy-to-maintain authentication system.

---

### Start Securing Your Application Today! 🔐
Get your users registered and authenticated with ease using this simple yet powerful domain! 💪
