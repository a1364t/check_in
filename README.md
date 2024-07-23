# Check-In Application

## Overview

This is a check-in application built using the Django web framework. The application allows users to check in to events or locations and provides an easy way to manage check-in data. Additionally, it captures user information and sends a welcome email with PDF attachments upon registration.

## Features

- Visitor check-in functionality
- Welcome email with PDF attachments sent upon user registration
- Admin panel for managing users
- Responsive design for mobile and desktop

## Technologies Used

- Django
- HTML/CSS
- Bootstrap
- SQLite (default databas)
- SMTP for email functionality

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/check-in-application.git
   cd check-in-application

2. Create a virtual environment:
    ```bash
    python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt

4.Apply the migration:
    ```bash
    python manage.py migrate

5. Run development server:
    ```bash
    python manage.py runserver

6. Create a super user to access the admin pannel
    ```bash
    python manage.py createsuperuser

7. Open your browser and go to http://127.0.0.1:8000/visitors to see the application in action.

## Usage

- **Visitors check-in**: Visitors can register to the application to check-in. Upon successful registration, a welcome email with PDF attachments is sent to the user's email address.

- **Admin Panel**: Admin users should sign up first. Authenticated user can see all users information categorised by date, including users check-in and check-out time.




