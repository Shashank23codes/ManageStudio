# ManageStudio

A professional photography studio management system built with HTML, CSS, JavaScript frontend and Python Flask backend with MongoDB database.

## Project Structure

```
ManageStudio/
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── images/
│   └── templates/
│       └── index.html
│
├── backend/
│   ├── app.py
│   ├── config/
│   │   └── config.py
│   ├── models/
│   │   └── __init__.py
│   ├── routes/
│   │   └── __init__.py
│   └── services/
│       └── __init__.py
│
├── requirements.txt
└── README.md
```

## Features

- Responsive web design with mobile-first approach
- Professional photography service packages
- Online booking system with package selection
- Interactive portfolio showcase
- Contact form with form validation
- Mobile-friendly interface with responsive navigation
- MongoDB integration for data persistence
- Static file serving for assets
- Template rendering with Flask
- Smooth scroll animations
- Custom CSS animations and transitions
- Professional pricing packages
- Date and time picker for booking
- Special requirements input option

## Technologies Used

### Frontend:

- HTML5
- CSS3
- JavaScript (ES6+)
- Responsive Design
- Custom Animations
- Dynamic Form Handling
- Interactive UI Components

### Backend:

- Python 3.x
- Flask 2.0.1
- PyMongo 3.12.0
- RESTful API Design
- Template Engine

### Database:

- MongoDB

## Photography Services

### Basic Portrait Package (₹199)

- 1 Hour Session
- Professional Photography
- 2 Outfit Changes
- 10 Edited Digital Photos
- Online Gallery Access
- Basic Retouching

### Wedding Package (₹1499)

- 6 Hours Coverage
- 2 Professional Photographers
- 200+ Edited Photos
- Premium Photo Album
- Online Gallery Access
- Advanced Retouching

### Fashion Portfolio (₹599)

- 3 Hours Session
- Studio Photography
- 4 Outfit Changes
- 30 Edited Photos
- Digital & Print Delivery
- Professional Retouching

## Setup and Installation

1. Clone the repository
2. Install Python 3.x if not already installed
3. Install MongoDB and ensure it's running on localhost:27017
4. Install required dependencies:

```
pip install -r requirements.txt
```

## Running the Application

1. Start MongoDB service
2. Navigate to the project directory
3. Run the Flask application:

```
python backend/app.py
```

4. Access the application at http://localhost:5000

## Development

### Frontend Structure

- static/css/ : Contains all styling files
  - style.css : Main stylesheet
  - booking.css : Booking page specific styles
- static/js/ : JavaScript files
  - main.js : Main JavaScript functionality
- templates/ : HTML templates
  - index.html : Home page
  - booking.html : Booking system page

### Backend Structure

- app.py : Main application file
- config/ : Configuration files
- models/ : Database models
- routes/ : Route handlers
- services/ : Business logic

### Key Features Implementation

- Responsive navigation system
- Dynamic form handling
- Interactive pricing cards
- Custom date and time picker
- Form validation
- Smooth scroll animations
- Portfolio filtering system
- Contact form processing

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## Author

- Shashank Gupta
