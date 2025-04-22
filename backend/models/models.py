from datetime import datetime
from pymongo import MongoClient
from config.config import Config

# MongoDB connection using config file
client = MongoClient(Config.MONGO_URI)
db = client[Config.DATABASE_NAME]

# Contact Form Model
class Contact:
    def __init__(self, name, email, subject, message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message
        self.created_at = datetime.utcnow()
    
    def save(self):
        return db.contacts.insert_one({
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message,
            'created_at': self.created_at
        })

# Booking Form Model
class Booking:
    def __init__(self, name, email, phone, package, date, time, message):
        self.name = name
        self.email = email
        self.phone = phone
        self.package = package
        self.date = date
        self.time = time
        self.message = message
        self.status = 'pending'  # pending, confirmed, cancelled
        self.created_at = datetime.utcnow()
    
    def save(self):
        return db.bookings.insert_one({
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'package': self.package,
            'date': self.date,
            'time': self.time,
            'message': self.message,
            'status': self.status,
            'created_at': self.created_at
        })