# django-openreg
Open-source authentication and user management API built with Django and DRF. Includes JWT auth, email verification, password reset, and role-based access.


## 🚀 Features

🔐 Custom User Model— built from scratch using Django’s AbstractBaseUser and BaseUserManager.
 
📩 Email Registration Workflow — register users and prepare them for future verification and notifications.

🧱 API-Ready Architecture — structured to support REST APIs and future frontend integration.

🌍 Open for Contributions — intentionally simple, with clean code and room for improvement.

📁 Modular Design — easy to extend with more features like login, QR codes, or password reset.

🧰 Tech Stack

Python 3.x

Django 4.x

SQLite / PostgreSQL (default: SQLite for development)

⚙️ Installation
## 1. Clone the repository
git clone https://github.com/Michael-oss138/django-openreg.git

## 2. Navigate into the project folder
cd django-openreg

## 3. Create a virtual environment
python -m venv venv

## 4. Activate the virtual environment
### On Windows:
venv\Scripts\activate
### On macOS/Linux:
source venv/bin/activate

## 5. Install dependencies
pip install -r requirements.txt

## 6. Run migrations
python manage.py migrate

## 7. Start the development server
python manage.py runserver

🧪 Usage

Once the server is running, open your browser and visit:

http://127.0.0.1:8000/


From here, you can start testing the user registration flow.
Future updates will include endpoints for login, profile management, and more.

🤝 Contributing

This project is intentionally built to be community-driven. If you want to learn Django, practice backend development, or collaborate on open source — you’re welcome to contribute.

Fork the repo 🍴

Create a new branch: git checkout -b feature-name

Make your changes and commit: git commit -m "Add new feature"

Push your branch: git push origin feature-name

Open a Pull Request ✅

📜 Roadmap

 Add login & logout

 Add email verification

 Add QR code generation

 Add REST API with Django REST Framework

 Add Docker support

Authr - Michael.
Built with ❤️ and a passion for open source.

📜 License

This project is licensed under the MIT License — free to use, modify, and distribute.
>>>>>>> de557bd (Worked on the README file)
