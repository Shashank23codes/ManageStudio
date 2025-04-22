from flask import Blueprint, request, jsonify
from models.models import Contact, Booking
from datetime import datetime

api = Blueprint('api', __name__)

@api.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()
        contact = Contact(
            name=data['name'],
            email=data['email'],
            subject=data['subject'],
            message=data['message']
        )
        contact.save()
        return jsonify({'message': 'Message sent successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@api.route('/api/booking', methods=['POST'])
def booking():
    try:
        data = request.get_json()
        booking = Booking(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            package=data['package'],
            date=datetime.strptime(data['date'], '%Y-%m-%d'),
            time=data['time'],
            message=data.get('message', '')
        )
        booking.save()
        return jsonify({'message': 'Booking submitted successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400