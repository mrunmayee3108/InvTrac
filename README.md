# InvTrac: Inventory Management System (FastAPI + React)

<p align="left">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
</p>

<p align="left">
  <b>Tech Stack:</b><br/>
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=flat-square" />
  <img src="https://img.shields.io/badge/Frontend-React-61DAFB?style=flat-square" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL-4169E1?style=flat-square" />
  <img src="https://img.shields.io/badge/ORM-SQLAlchemy-D71F00?style=flat-square" />
  <img src="https://img.shields.io/badge/Server-Uvicorn-333333?style=flat-square" />
</p>

A full‑stack **Inventory Management System** built using **FastAPI** for the backend and **React** for the frontend. This project allows users to manage products with features like adding, viewing, editing, deleting, and searching inventory items, all backed by a **PostgreSQL** database.


## 🚀 Features

* Add new products (ID, name, description, price, quantity)
* View all products in a clean tabular UI
* Edit existing product details
* Delete products
* Search products by ID, name, or description
* Persistent storage using PostgreSQL
* RESTful API built with FastAPI
* Modern React UI


## 🛠️ Tech Stack

### Backend

* **FastAPI**
* **Python**
* **SQLAlchemy**
* **PostgreSQL**
* **Uvicorn**

### Frontend

* **React.js**
* **JavaScript (ES6+)**
* **CSS**
* **Axios / Fetch API**


## 📁 Project Structure

```
FASTAPI-INVENTORY/
│
├── frontend/
│   ├── node_modules/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   ├── index.css
│   │   ├── TaglineSection.js
│   │   └── TaglineSection.css
│   ├── package.json
│   └── package-lock.json
│
├── myenv/                 # Python virtual environment
├── main.py                # FastAPI entry point
├── database.py            # Database connection setup
├── models.py              # SQLAlchemy models
├── database_models.py     # Table definitions
├── __pycache__/
└── README.md
```


## ⚙️ Setup Instructions

### 1️⃣ Backend Setup (FastAPI)

```bash
# Create virtual environment
python -m venv myenv

# Activate virtual environment
# Windows
myenv\Scripts\activate
# macOS/Linux
source myenv/bin/activate

# Install dependencies
pip install fastapi uvicorn sqlalchemy psycopg2-binary

# Run FastAPI server
uvicorn main:app --reload
```

FastAPI will run at:
👉 `http://127.0.0.1:8000`

API Docs:

* Swagger UI: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`


### 2️⃣ Frontend Setup (React)

```bash
cd frontend
npm install
npm start
```

React app will run at:
👉 `http://localhost:3000`


## 🗄️ Database

* **Database:** PostgreSQL
* **Table:** `Product_db`

### Sample Columns

* `id` (Primary Key)
* `name`
* `description`
* `price`
* `quantity`

You can manage and view data using **pgAdmin 4**.


## 🔄 API Overview

| Method | Endpoint         | Description        |
| ------ | ---------------- | ------------------ |
| GET    | `/products`      | Fetch all products |
| POST   | `/products`      | Add a new product  |
| PUT    | `/products/{id}` | Update a product   |
| DELETE | `/products/{id}` | Delete a product   |

---

## 📸 Screenshots

* React dashboard displaying inventory
  <img width="1905" height="970" alt="image" src="https://github.com/user-attachments/assets/c16256a4-5c33-4926-8949-34385c8506a8" />

* Add/Edit/Delete product functionality
  <img width="795" height="839" alt="image" src="https://github.com/user-attachments/assets/a94b47d7-7762-42b5-a149-326d9d95d13e" />

  <img width="1918" height="969" alt="image" src="https://github.com/user-attachments/assets/f6cb4f6f-0f84-41b0-93da-c5ffcd508bb0" />

* Update functionality
  <img width="1919" height="943" alt="image" src="https://github.com/user-attachments/assets/0e704a1b-b29e-437e-90a4-16e3c322d8dc" />


* PostgreSQL data synced with UI
  <img width="1919" height="1023" alt="image" src="https://github.com/user-attachments/assets/6d056d1a-418c-498c-b519-586811c7b03e" />



## 🌱 Future Enhancements

* User authentication (JWT)
* Role‑based access control
* Pagination & sorting
* Category‑wise inventory
* Low‑stock alerts
* Deployment (Docker / AWS)


## 👩‍💻 Author

**Mrunmayee Potdar**


## ⭐ Acknowledgements

* FastAPI Documentation
* React Documentation
* PostgreSQL


⭐ If you like this project, give it a star!
