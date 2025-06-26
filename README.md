# Flask MongoDB CRUD App (User Management API)

This is a Flask-based REST API project for managing users — simple but solid. It covers the full CRUD cycle (Create, Read, Update, Delete) and hooks up with MongoDB via Docker. It includes basic validation, password hashing, and clean endpoints. Ideal for learning, demonstrating API design, or spinning up a user service quickly.

## Features

* Register new users with hashed passwords
* List all users (excluding passwords for security)
* Update user fields individually or together
* Delete users cleanly
* Input validation for email format (with `.com` requirement)
* Dockerized for easy local setup

## Technologies Used

* **Flask** – Lightweight Python web framework
* **MongoDB** – NoSQL database to store user data
* **Flask-PyMongo** – For DB integration
* **Flask-Bcrypt** – Secure password hashing
* **email-validator** – Ensures valid and realistic emails
* **Docker + Docker Compose** – Runs everything with one command

## User Model (sample data)

```json
{
  "name": "Keshav",
  "email": "something@gmail.com",
  "password": "<bcrypt hashed>"
}
```

## API Endpoints

Use Postman or any REST client to interact with the API:

| Method | Endpoint      | Purpose            |
| ------ | ------------- | ------------------ |
| GET    | `/users`      | List all users     |
| GET    | `/users/<id>` | Fetch single user  |
| POST   | `/users`      | Create new user    |
| PUT    | `/users/<id>` | Update user fields |
| DELETE | `/users/<id>` | Remove user by ID  |

---





AND the main thing comes here, the email vaiddator 

-->> If you enter an email which does not end with .com it will give you an error
![image](https://github.com/user-attachments/assets/9f2df8a9-6b5f-4f7c-8624-ea0b1dd751dc)


-->> If you enter an email which is not of correct sequence after the "@" , it will give you an error
![image](https://github.com/user-attachments/assets/c905864f-7a91-4d5a-a002-99898865fd64)

-->> If you create it with no errors , it will let you proceed
![image](https://github.com/user-attachments/assets/c7f69200-7526-4391-9299-84c2e9687999)


AND ONE MORE THING

The password which you enter will be hashed and then stored in the Mongodb database,and when you wnat to check, the password will be re-hashed and compared 
<img width="798" alt="Screenshot 2025-06-26 at 6 01 15 PM" src="https://github.com/user-attachments/assets/bfaad94d-d57c-4939-8534-adc7f0682e20" />


<img width="914" alt="Screenshot 2025-06-26 at 6 01 47 PM" src="https://github.com/user-attachments/assets/eff930b6-d2c4-489f-911a-cb808821652c" />


## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-name/your-repo.git
cd your-repo
```

### 2. Build and Run

Ensure Docker is installed and running, then:

```bash
docker compose up --build
```

> The Flask server will start on:

```
http://localhost:5000 (or 5050 if port mapping was changed)
```

---

## Example Requests

### Create a User (POST `/users`)

```json
{
  "name": "Alice",
  "email": "alice@gmail.com",
  "password": "SecurePass123"
}
```

### Update a User (PUT `/users/<id>`)

```json
{
  "name": "Alice Updated",
  "email": "newalice@gmail.com"
}
```

### Get Users (GET `/users`)

* Returns a list of users without their passwords.

### Delete User (DELETE `/users/<id>`)

* Just send the request. If the ID exists, it deletes.

---

## Notes

* All passwords are securely hashed using Bcrypt.
* Emails must be `.com` addresses and pass validation.
* Invalid or incomplete data returns clear 400 or 404 errors.
* Works well with Postman, curl, or any frontend you want to add.

---
