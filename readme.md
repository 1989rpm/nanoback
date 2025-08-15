# MINT Lab Backend

This is the backend service for the MINT (Molecular Imaging & Interventional Theranostics) Lab website.  
It is built using **Django** and **Django REST Framework**, with **PostgreSQL** as the database.

---

## 📦 Tech Stack
- **Python** 3.12+
- **Django** 5.2
- **Django REST Framework**
- **PostgreSQL**
- **Pillow** for image handling
- **django-cors-headers** for cross-origin requests

---

## 🛠️ Prerequisites
Before running the backend, ensure you have:
- **Python** (>= 3.10 recommended)
- **PostgreSQL** installed and running
- **Git** installed
- **pip** (Python package manager)
- (Optional) **virtualenv** for isolated environments

---

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/mint-lab-backend.git
cd mint-lab-backend
2. Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Configure database settings
Update the DATABASES section in settings.py with your PostgreSQL credentials:

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_postgres_user',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Note: Make sure you have created the database in PostgreSQL:

bash
Copy
Edit
psql -U postgres
CREATE DATABASE your_database_name;
5. Run migrations
bash
Copy
Edit
python manage.py migrate
6. Create a superuser (admin)
bash
Copy
Edit
python manage.py createsuperuser
7. Run the development server
bash
Copy
Edit
python manage.py runserver
📂 Project Structure
csharp
Copy
Edit
mint-lab-backend/
│
├── app_name/            # Your Django apps
├── media/               # Uploaded images & files
├── static/              # Static files (if collected)
├── manage.py
├── requirements.txt
└── README.md
🌐 API Access
Once running, the backend will be available at:

cpp
Copy
Edit
http://127.0.0.1:8000/
API endpoints will be available under /api/ or as defined in your urls.py.

🛡️ Environment Variables (Recommended)
Instead of editing settings.py directly, use a .env file and load it with python-decouple or similar:

ini
Copy
Edit
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_database_name
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
📜 Running in Production
Use Gunicorn or uWSGI as the application server.

Serve static files using Whitenoise or Nginx.

Set DEBUG=False and configure ALLOWED_HOSTS in settings.py.

Apply migrations on the server:

bash
Copy
Edit
python manage.py migrate
📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

👨‍💻 Author
Rahul Kumar
Biochemical Engineering, IIT BHU

