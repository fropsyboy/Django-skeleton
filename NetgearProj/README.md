# Django Authentication with JWT and MaxMin API

This Django project demonstrates user authentication using JWT (JSON Web Tokens) and a simple API for finding the maximum and minimum values in an array of integers. It features user registration, login, and a max-min API that requires authentication.

## Table of Contents
- [Dependencies](#dependencies)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
    - [Register](#register)
    - [Login](#login)
    - [MaxMin](#maxmin)
- [Usage](#usage)
- [Notes](#notes)

## Dependencies

- Django
- Django Rest Framework
- djangorestframework-simplejwt

## Installation

1. Create a virtual environment and activate it:

\`\`\`
python -m venv venv
venv\Scripts\activate (Windows)
source venv/bin/activate (Linux/macOS)
\`\`\`

2. Install the required dependencies using the `requirements.txt` file:

\`\`\`
pip install -r requirements.txt
\`\`\`

3. Apply the migrations:

\`\`\`
python manage.py makemigrations
python manage.py migrate
\`\`\`

4. Run the development server:

\`\`\`
python manage.py runserver
\`\`\`

## API Endpoints

### Register

- Endpoint: `/auth/register/`
- Method: `POST`
- Requires authentication: No
- Payload:
    - `username` (string): The desired username for the new user.
    - `password` (string): The password for the new user.
- Response: A new user is created, and the user is logged in.

### Login

- Endpoint: `/auth/login/`
- Method: `POST`
- Requires authentication: No
- Payload:
    - `username` (string): The username of the existing user.
    - `password` (string): The password of the existing user.
- Response: If the credentials are valid, the JWT access and refresh tokens are returned.

### MaxMin

- Endpoint: `/auth/max_min/`
- Method: `POST`
- Requires authentication: Yes
- Payload:
    - `array` (list of integers): An array of integers to find the maximum and minimum values.
- Response: The maximum and minimum values in the input array are returned.

## Usage

1. Register a new user by making a `POST` request to `/auth/register/` with the `username` and `password` fields in the payload.

2. Log in with the registered user by making a `POST` request to `/auth/login/` with the `username` and `password` fields in the payload. If the credentials are valid, the JWT access and refresh tokens are returned.

3. Make a `POST` request to `/auth/max_min/` with an array of integers in the payload. Set the `Authorization` header to `Bearer {access_token}` (replace `{access_token}` with the actual access token from the login response). If the user is authenticated, the maximum and minimum values in the input array are returned.

## Notes

- In a production environment, make sure to replace the `SECRET_KEY` in `my_auth_project/settings.py` with a secure secret key and set `DEBUG = False`.
- The default user model is extended with the `CustomUser` model in `authentication/models.py`. You can add additional fields to the `CustomUser` model as needed.
- The JWT token expiration times can be customized in the project settings. Refer to the [djangorestframework-simplejwt documentation](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html) for more information.
-
