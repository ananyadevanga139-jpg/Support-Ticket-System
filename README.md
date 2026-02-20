🎫 Support Ticket System

A full-stack Support Ticket Management System built using Django and Django REST Framework.
This system allows users to create, manage, and track support tickets efficiently.

🚀 Features

User Registration & Authentication

Create Support Tickets

Update Ticket Status

View All Tickets

RESTful API using Django REST Framework

Backend structured with clean architecture

🛠️ Tech Stack

🐍 Python

🌐 Django (4.2)

🔗 Django REST Framework (3.16.1)

🗄️ SQLite (Default Database)

⚙️ Virtual Environment (venv)

📂 Project Structure
support-ticket-system/
│
├── backend/
│   ├── config/          # Project settings
│   ├── tickets/         # Ticket app
│   ├── manage.py
│   └── requirements.txt
│
└── frontend/ (if added)
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/support-ticket-system.git
cd support-ticket-system/backend
2️⃣ Create Virtual Environment
python -m venv venv

Activate it:

Windows (PowerShell)

.\venv\Scripts\Activate.ps1
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Run the Server
python manage.py runserver

Server runs at:
👉 http://127.0.0.1:8000/

📡 API Endpoints (Example)
Method	Endpoint	Description
GET	/api/tickets/	View all tickets
POST	/api/tickets/	Create new ticket
PUT	/api/tickets/{id}/	Update ticket
DELETE	/api/tickets/{id}/	Delete ticket
🎯 Future Improvements

Role-based access control

Email notifications

Dashboard analytics

Deployment on cloud (AWS/Render/Heroku)

👩‍💻 Author

Ananya K
 Artificial Intelligence and Machine Learning Enthusiast
