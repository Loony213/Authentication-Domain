
# 🔐 Login Service

This microservice is part of the real-time chat distributed system. It handles **user login** functionalities.

---

## 📌 What does it do?

- 🔑 Authenticates users via credentials
- 🔒 Validates users in the system
- 📤 Exposes RESTful API endpoints to be consumed by the React frontend or other services

---

## 🧩 Architecture

- 🧱 **Style**: Independent microservice
- 🌐 **API**: REST (FastAPI)
- 🐍 **Language**: Python 3.11+
- 🐳 **Container**: Dockerized for easy deployment

---

## 📁 Project Structure

```
.
├── controllers/            # Business logic
├── models/                 # Data models for the service
├── routes/                 # FastAPI routes for the service
├── services/               # Service-related logic
├── utils/                  # Utility functions for the service
├── app.py                  # Main entry point with FastAPI routes
├── Dockerfile              # Docker image of the microservice
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 🚀 How to Deploy

### 🐳 Using Docker

1. **Clone the repository**:

```bash
git clone https://github.com/Loony213/Login-Service.git
cd Login-Service
```

2. **Build the Docker image**:

```bash
docker build -t kamartinez/login-service .
```

3. **Run the container**:

```bash
docker run -d -p 8001:8001 kamartinez/login-service
```

The API will be available at:  
📍 `http://localhost:8001`

---

## 🧪 Main Endpoints

- `POST /login` → Logs in and validates credentials

---

## 🔗 Integrations

- 🔐 Connects to SQL Server on RDS (AWS)
- 🧩 Communicates with the React frontend and other microservices

---

## 🛠️ Requirements

- Python 3.11+
- Docker
- Database access with environment variables configured

---

## 👤 Author

Developed by **Loony213**  
Domain: `Login-Service`  
Part of the **Distributed Chat System**

