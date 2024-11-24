Employee Management System
Overview
This project is a complete Employee Management System, allowing users to manage employees
dynamically with customizable forms. It is built with Django (Python) for the backend and React.js for
the frontend.
The system provides features like authentication, profile management, dynamic form creation, and
CRUD operations for employees. REST APIs are implemented for all major functionalities, ensuring
seamless communication between the backend and frontend.
Features
Authentication and Profile Management
- Login & Registration: Secure JWT-based authentication.
- Change Password: Allow users to update their password securely.
- User Profile: View and update user details.
Employee Management
- Dynamic Form Builder: Build and edit forms with customizable fields.
- Employee Creation and Update: Use pre-built forms to add or update employee details.
- Employee Listing: View a searchable and filterable list of employees.
API Development
- Secure REST APIs for user login and registration.
- Employee CRUD operations and dynamic form management.
Technology Stack
- Backend: Django (Python), Django REST Framework (DRF)
- Frontend: React.js, Tailwind CSS
- Database: SQLite (can be swapped for PostgreSQL or other RDBMS)
- Authentication: JWT (Access & Refresh tokens)
- State Management: Redux Toolkit
- Styling: Tailwind CSS
- APIs: Axios (for frontend API requests)
Installation and Setup
Backend Setup
- Clone the repository: git clone <repo_url>
- Set up a Python virtual environment: python -m venv env
- Install dependencies: pip install -r requirements.txt
- Apply database migrations: python manage.py migrate
- Run the development server: python manage.py runserver
Frontend Setup
- Navigate to the frontend directory: cd frontend
- Install dependencies: npm install
- Start the React development server: npm start
Usage Instructions
1. Start the backend server (Django): python manage.py runserver
2. Start the frontend server (React): cd frontend && npm start
3. Access the application at: http://localhost:3000 (frontend) and http://127.0.0.1:8000 (backend).
Endpoints and Use Cases
Authentication
- /auth/register/ - POST: Register a new user
- /auth/login/ - POST: Login and get JWT tokens
- /auth/change-password/ - PUT: Change user password
- /auth/user/ - GET: Fetch authenticated user
Dynamic Form
- /api/forms/ - POST: Create a dynamic form
- /api/forms/<id>/ - GET: Fetch a specific form
- /api/forms/<id>/ - PUT: Update a form
- /api/forms/<id>/ - DELETE: Delete a form
Employee Management
- /api/employees/ - POST: Add a new employee
- /api/employees/ - GET: List all employees
- /api/employees/<id>/ - GET: Fetch a specific employee record
- /api/employees/<id>/ - PUT: Update an employee record
- /api/employees/<id>/ - DELETE: Delete an employee record
