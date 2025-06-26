# Flask MongoDB CRUD App (user management thing)

So yeah, this is a simple Flask app that does basic user operations - like adding, updating, deleting people from a MongoDB. All via HTTP. It’s Dockerized. You can test stuff in Postman.

## What's inside?

* You can create a user
* See all users (except their passwords)
* Edit a user’s name/email/password
* Delete a user

## Tech used

* Flask (obviously)
* MongoDB (running in Docker)
* Flask-PyMongo to connect Flask and Mongo
* Flask-Bcrypt for hashing passwords
* email-validator so people don’t type fake stuff
* Docker & Docker Compose for running the thing without pain

## User data looks like:

```
{
  "name": "Keshav",
  "email": "something@gmail.com",
  "password": "hashed in db don’t worry"
}
```

## Routes

Just use these in Postman:

* `GET /users` → get everyone
* `GET /users/<id>` → just one user
* `POST /users` → make a new user
* `PUT /users/<id>` → update stuff
* `DELETE /users/<id>` → boom, user gone


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



## Setup

1. Clone this project:

```bash
git clone https://github.com/your-name/your-repo.git
cd your-repo
```

2. Run everything (you need Docker running):

```bash
docker compose up --build
```

Flask app will be live on:

```
http://localhost:5000 (or maybe 5050 if you changed port)
```

## Testing with Postman

You can test all of it easily:

### Add a user:

POST to `/users`

```json
{
  "name": "Someone",
  "email": "someone@gmail.com",
  "password": "notplain"
}
```

### Get all users:

GET `/users`

### Edit user:

PUT `/users/<id>`

```json
{
  "name": "New Name"
}
```

### Delete:

DELETE `/users/<id>`

## Notes

* All passwords are hashed with bcrypt
* Emails must be real `.com` ones, no `abc@xyz.fake`
* If you send garbage input, it’ll reject it politely

## Submitting?

* Code ✅
* Docker ✅
* API works ✅
* This README ✅ (I guess?)
* Push to GitHub ✅

Paste GitHub link below:

```
https://github.com/your-name/your-repo
```

That’s it. If anything breaks, try again. It worked for me :)
