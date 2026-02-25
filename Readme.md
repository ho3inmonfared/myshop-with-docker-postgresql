🛒 MyShop – Django E-commerce with Docker & PostgreSQL

A step-by-step fully containerized e-commerce project built from scratch using:

🐍 Python

🌿 Django

🐘 PostgreSQL

🐳 Docker & Docker Compose

🎨 HTML & CSS

🔐 Django Built-in Authentication

🔧 Git & GitHub

This project is designed as a practical, real-world learning experience for building a production-ready Django application.

🚀 Features

User Authentication (Login / Register / Logout)

Django Admin Panel

Product Management

Product Categories

Product Status with Django Choices

PostgreSQL Database Integration

Fully Dockerized Setup

Clean & Modular Project Structure

Ready for Future Scaling

🧱 Tech Stack
Technology	Purpose
Python	Backend Logic
Django	Web Framework
PostgreSQL	Database
Docker	Containerization
Docker Compose	Multi-container Orchestration
HTML / CSS	Frontend
GitHub	Version Control
🐳 Running the Project with Docker (Recommended)
1️⃣ Clone the Repository
git clone https://github.com/ho3inmonfared/myshop-with-docker-postgresql.git
cd myshop-with-docker-postgresql
2️⃣ Build the Containers
docker compose build
3️⃣ Run the Project
docker compose up
4️⃣ Open in Your Browser
http://localhost:8000
🗄 Database

This project uses PostgreSQL running inside Docker.
No need to install PostgreSQL locally.

🔐 Authentication System

Built using Django's built-in authentication system:

User Registration

Login / Logout

Session Handling

Protected Views

Admin Authentication

🛠 Running Without Docker (Optional)

If you prefer running locally without Docker:

python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
📂 Project Structure (Simplified)
myshop/
 ├── products/
 ├── users/
 ├── templates/
 ├── static/
 ├── docker-compose.yml
 ├── Dockerfile
 └── manage.py
🎯 Project Goals

This project was built to:

Practice Django in a real-world scenario

Learn Docker in a practical way

Connect Django with PostgreSQL

Build a production-ready structure

Create a strong portfolio project

🚀 Future Improvements

Shopping Cart System

Payment Gateway Integration

Order Management

Product Reviews & Ratings

Search & Filtering

Analytics Dashboard

Responsive UI Improvements

🤝 Contributing

Contributions are welcome!
Feel free to fork the project and submit a Pull Request.

👨‍💻 Author

Hossein Monfared

⭐ Support

If you found this project helpful:

⭐ Star the repository

🍴 Fork it

📢 Share it