from flask import Flask, render_template
from pymongo import MongoClient
from config.config import Config

app = Flask(__name__, 
            static_folder='../frontend/static',
            template_folder='../frontend/templates')

# MongoDB connection using config file
client = MongoClient(Config.MONGO_URI)
db = client[Config.DATABASE_NAME]
app.debug = Config.DEBUG

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for the booking page
@app.route('/booking')
def booking():
    return render_template('booking.html')

if __name__ == '__main__':
    app.run(debug=True)