
# 🔐 Authentication-Domain

This microservice is part of the real-time chat distributed system. It handles **user authentication**, including **login** and **registration** functionalities.

---

## 📌 What does it do?

- ✅ Registers new users
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
├── .github/workflows       # CI/CD workflows
├── Login/                  # Login logic
├── Register/               # User registration logic
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
git clone https://github.com/your_user/Authentication-Domain.git
cd Authentication-Domain
```

2. **Build the Docker image**:

```bash
docker build -t kamartinez/authentication-domain .
```

3. **Run the container**:

```bash
docker run -d -p 8000:8000 kamartinez/authentication-domain
```

The API will be available at:  
📍 `http://localhost:8000`

---

## 🧪 Main Endpoints

- `POST /register` → Registers a new user
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
Domain: `Authentication-Domain`  
Part of the **Distribuida** distributed system
