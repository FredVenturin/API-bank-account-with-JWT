# Bank Account API with JWT

A RESTful API built with **Flask** that simulates a simple banking system, allowing users to create accounts and perform operations securely using **JWT (JSON Web Token) authentication**.

This project was developed for educational purposes to explore backend development concepts such as authentication, authorization, API design, and secure data handling.

---

## Overview

The Bank Account API provides a basic simulation of a banking system where users can:

- create accounts
- authenticate securely
- access protected endpoints
- perform operations on their accounts

Authentication is handled using **JWT**, meaning that after login, the user receives a token that must be included in future requests to access protected resources.

This project demonstrates how modern APIs handle stateless authentication and secure access control.

---

## Main Features

- User registration
- Secure login with JWT authentication
- Token-based authorization
- Protected API routes
- Bank account creation
- Basic account operations (such as balance handling)
- Organized backend structure using Flask
- Study-focused implementation of authentication and API security

---

## Technologies Used

- **Python**
- **Flask**
- **Flask-JWT-Extended** (or similar JWT library)
- **SQLite / SQLAlchemy**
- **Werkzeug Security** or **bcrypt**
- **REST API principles**

---

## How JWT Authentication Works

The API uses **JWT (JSON Web Token)** for authentication.

### Authentication Flow

1. The user registers with username and password  
2. The password is securely stored (hashed)  
3. The user logs in  
4. The API generates a JWT token  
5. The client stores the token  
6. The token is sent in the `Authorization` header for protected requests  

Example:
