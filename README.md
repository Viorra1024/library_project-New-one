# 📚 Library Management System (Django)

A role-based library system with book borrowing rules for students and pupils. Supports admin panel, file import/export, serialization with pickle, and custom logic for borrowing permissions.

---

## ✅ Setup Instructions (macOS & Linux)

1. **Clone the project** or download ZIP  
2. **Navigate to the project folder**:
   ```bash
   cd library_project

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```
Run database migrations:


```bash
python manage.py migrate
```
Start the development server:

```bash
python manage.py runserver
```
Open in browser:
```bash
http://127.0.0.1:8000/