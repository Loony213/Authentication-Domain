
# 🔐 Register Service

This microservice is part of the real-time chat distributed system. It handles **user registration** functionality.

---

## 📌 What does it do?

- ✅ Registers new users
- 🔒 Validates user data
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
├── controllers/            # Registration logic
├── models/                 # Data models for users
├── routes/                 # FastAPI routes for registration
├── services/               # Business logic for user registration
├── utils/                  # Helper functions
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
git clone https://github.com/Loony213/Register-Service.git
cd Register-Service
```

2. **Build the Docker image**:

```bash
docker build -t kamartinez/register-service .
```

3. **Run the container**:

```bash
docker run -d -p 8002:8002 kamartinez/register-service
```

The API will be available at:  
📍 `http://localhost:8002`

---

## 🧪 Main Endpoints

- `POST /register` → Registers a new user

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
Domain: `Register-Service`  
Part of the **Distribuida** distributed system
