
# 📝 Register Module

This module is part of the `Authentication-Domain` microservice. It is responsible for handling **new user registration** within the system.

---

## 📌 What does it do?

- 🧍‍♂️ Accepts user data (username, email, password, etc.)
- 🛡️ Validates input format and uniqueness
- 🗂️ Stores the new user in the database
- 🧩 Serves the `/register` endpoint within the microservice

---

## 🧩 Architecture

- 📂 Folder: `Register/`
- 🐍 Language: Python 3.11+
- 🧱 Style: Modular code inside the microservice

---

## 📁 Files

```
Register/
├── __pycache__/       # Compiled Python cache files
└── register.py        # Main registration logic (input validation and DB insert)
```

---

## 📤 Integration

This module is called from `app.py` as part of the REST endpoint `POST /register`.

---

## 🔗 Dependencies

- Connection to the user database (SQL Server)
- Input sanitization and password hashing tools, if used

---

## 👤 Author

Developed by **Loony213**  
Part of the `Authentication-Domain` microservice  
Distributed system **Distribuida**
