# 🚀 Job Board Backend – ProDev BE

A production-ready Job Board Backend built using **Django**, **PostgreSQL**, JWT authentication, and Swagger API documentation.

This backend provides role-based access control, optimized job search filtering, and a scalable modular architecture suitable for real-world job platforms.

---

# 📌 Project Overview

The Job Board Backend is designed to support:

* Job posting management
* Category management
* Role-based authentication (Admin & User)
* Job applications
* Advanced filtering and optimized search
* API documentation via Swagger

This project demonstrates:

* Clean architecture
* Secure authentication
* Database optimization
* Scalable backend structure

---

# 🏗️ Tech Stack

| Technology            | Purpose               |
| --------------------- | --------------------- |
| Django                | Backend framework     |
| Django REST Framework | API development       |
| PostgreSQL            | Database              |
| SimpleJWT             | JWT Authentication    |
| drf-yasg              | Swagger documentation |
| django-filter         | Advanced filtering    |

---

# 📁 Project Structure

```
job_board_backend/
│
├── config/
├── apps/
│   └── jobs/
│       ├── models/
│       ├── serializers/
│       ├── views/
│       ├── permissions/
│       ├── filters/
│       ├── urls.py
│
├── core/
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🔐 Authentication & Roles

## 👤 Roles

### 🔹 Admin

* Create, update, delete jobs
* Manage categories

### 🔹 User

* View jobs
* Filter jobs
* Apply for jobs
* View applications

Authentication is handled using JWT:

* `POST /api/token/`
* `POST /api/token/refresh/`

---

# 📚 API Endpoints

## 🔑 Authentication

| Method | Endpoint              | Description      |
| ------ | --------------------- | ---------------- |
| POST   | `/api/auth/register/` | Register user    |
| POST   | `/api/token/`         | Obtain JWT token |
| POST   | `/api/token/refresh/` | Refresh token    |

---

## 📂 Categories

| Method | Endpoint                | Access |
| ------ | ----------------------- | ------ |
| GET    | `/api/categories/`      | Public |
| POST   | `/api/categories/`      | Admin  |
| PUT    | `/api/categories/{id}/` | Admin  |
| DELETE | `/api/categories/{id}/` | Admin  |

---

## 💼 Jobs

| Method | Endpoint          | Access |
| ------ | ----------------- | ------ |
| GET    | `/api/jobs/`      | Public |
| GET    | `/api/jobs/{id}/` | Public |
| POST   | `/api/jobs/`      | Admin  |
| PUT    | `/api/jobs/{id}/` | Admin  |
| DELETE | `/api/jobs/{id}/` | Admin  |

---

## 📄 Applications

| Method | Endpoint             | Access |
| ------ | -------------------- | ------ |
| POST   | `/api/applications/` | User   |
| GET    | `/api/applications/` | User   |

Duplicate applications are prevented using a unique constraint.

---

# 🔎 Job Filtering

Optimized filtering supported via query parameters:

```
/api/jobs/?title=developer
/api/jobs/?location=Addis
/api/jobs/?category=IT
/api/jobs/?job_type=FULL_TIME
```

Database indexing is applied to:

* location
* category
* created_at

This ensures fast search performance.

---

# 📑 API Documentation

Swagger documentation available at:

```
/api/docs/
```

Provides:

* Interactive testing
* Request/Response schemas
* Authentication testing

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd job_board_backend
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create `.env` file:

```
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=job_board
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
```

---

## 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

## 7️⃣ Run Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/api/docs/
```

---

# 🚀 Deployment

The project can be deployed on:

* Render
* Railway
* Heroku
* Any VPS with PostgreSQL

Make sure to set:

* `DEBUG=False`
* `ALLOWED_HOSTS`
* Production PostgreSQL database

---

# 📊 Database Design (ERD Overview)

Entities:

* User (Custom)
* Category
* Job
* Application

Relationships:

* Job → Category (Many-to-One)
* Job → User (Admin creator)
* Application → User (Many-to-One)
* Application → Job (Many-to-One)

---

# 🏆 Key Features

✔ Role-based access control
✔ JWT authentication
✔ Modular architecture
✔ Optimized indexed search
✔ Swagger documentation
✔ Prevent duplicate applications
✔ Production-ready structure

---

# 📌 Evaluation Readiness

This project demonstrates:

* Clean Django architecture
* Proper separation of concerns
* Database normalization
* Query optimization
* Secure authentication
* Scalable backend design

---

# 👨‍💻 Author

**Ermias Dagnew**
Backend Developer – ProDev BE
