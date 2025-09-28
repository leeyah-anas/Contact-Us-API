# 📬 Contact Us API

A simple FastAPI + MongoDB backend for managing "Contact Us" form submissions.  
This project provides a REST API to create and manage contact messages.

---

## 🚀 Features
- Save contact form messages (Name, Email, Message) into MongoDB
- Auto-generated interactive API docs via **Swagger UI**
- Asynchronous DB operations using **Motor**
- Clean, modular project structure

---

## 🛠 Tech Stack
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [Uvicorn](https://www.uvicorn.org/) - ASGI server
- [MongoDB](https://www.mongodb.com/) - NoSQL database
- [Motor](https://motor.readthedocs.io/) - Async MongoDB driver

---

## 📂 Project Structure
CONTACT-US-API/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py          # Application settings and configuration
│   │   └── validation.py      # Custom Pydantic models
│   ├── db/
│   │   ├── __init__.py
│   │   └── mongodb.py         # MongoDB connection and operations
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── contact.py         # Contact data models
│   ├── services/
│   │   ├── __init__.py
│   │   └── contact.py         # Business logic for contact operations
│   └── v1/
│       ├── __init__.py
│       └── contact.py         # API route handlers
├── venv/                      # Virtual environment
├── .env                       # Environment variables
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation


---

## Prerequisites

Python 3.8+
MongoDB (local or cloud instance)
pip (Python package manager)

## Installation

1.Clone the repository
bashgit clone <repository-url>
cd CONTACT-US-API

2.Create and activate virtual environment
bash# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

3.Install dependencies
bashpip install -r requirements.txt

4.Set up environment variables
Create a .env file in the project root:

MONGODB_URI=mongodb://localhost:27017
DATABASE_NAME=vinovibe
CONTACT_COLLECTION=contacts
