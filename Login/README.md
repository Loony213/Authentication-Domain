
# 🔑 Login Module

This module is part of the `Authentication-Domain` microservice. Its main responsibility is to manage **user authentication** using credentials.

---

## 📌 What does it do?

- 🧍‍♂️ Checks if a user exists in the database
- 🔐 Validates credentials (username and password)
- 🧾 Returns authentication responses (success or failure)
- 🧩 Serves the `/login` endpoint within the microservice

---

## 🧩 Architecture

- 📂 Folder: `Login/`
- 🐍 Language: Python 3.11+
- 🧱 Style: Modular code inside the microservice

---

## 📁 Files

```
Login/
├── __pycache__/      # Compiled Python cache files
└── login.py          # Main login logic (verification and authentication)
```

---

## 📤 Integration

This module is called from `app.py` as part of the REST endpoint `POST /login`.

---

## 🔗 Dependencies

- Connection to the user database (SQL Server)
- Tools for password hashing or credential validation, if used

---

## 👤 Author

Developed by **Loony213**  
Part of the `Authentication-Domain` microservice  
Distributed system **Distribuida**
