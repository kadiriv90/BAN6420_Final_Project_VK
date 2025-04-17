# =============================================
# Import libraries
# =============================================

from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import csv
import os
import certifi
import datetime
import socket
import time
from werkzeug.serving import run_simple

app = Flask(__name__)

# =============================================
# MongoDB Configuration
# =============================================
MONGODB_URI = "mongodb+srv://Deev:Jasmine2708@cluster0.dnfhh8j.mongodb.net/healthcare_survey?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(
        MONGODB_URI,
        tlsCAFile=certifi.where(),
        connectTimeoutMS=30000,
        socketTimeoutMS=30000
    )
    client.admin.command('ping')
    db = client.healthcare_survey
    users_collection = db.users
    print("✅ Successfully connected to MongoDB Atlas")
except Exception as e:
    print(f"❌ MongoDB connection failed: {e}")
    raise SystemExit("Failed to connect to MongoDB - application stopping")

# =============================================
# User Class
# =============================================
class User:
    """Python class to represent survey user data"""
    
    def __init__(self, name, age, email, gender, income, expenses):
        """Initialize user with personal and financial data"""
        self.name = name.strip()
        self.age = age
        self.email = email.strip()
        self.gender = gender
        self.income = income
        self.expenses = expenses  # Dictionary of expense categories
        self.timestamp = datetime.datetime.utcnow()
    
    def calculate_metrics(self):
        """Calculate derived financial metrics"""
        total_spent = sum(self.expenses.values())
        return {
            'total_spent': total_spent,
            'savings': self.income - total_spent
        }
    
    def to_dict(self):
        """Convert User object to dictionary for storage"""
        metrics = self.calculate_metrics()
        return {
            'name': self.name,
            'age': self.age,
            'email': self.email,
            'gender': self.gender,
            'income': self.income,
            **self.expenses,
            'total_spent': metrics['total_spent'],
            'savings': metrics['savings'],
            'timestamp': self.timestamp
        }

# =============================================
# CSV Storage with Looping
# =============================================
def save_users_to_csv(users_data, filename='user_data.csv'):
    """Save multiple user records to CSV with proper headers"""
    file_exists = os.path.isfile(filename)
    
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        fieldnames = [
            'name', 'age', 'email', 'gender', 'income',
            'utilities', 'entertainment', 'school_fees',
            'shopping', 'healthcare', 'total_spent', 'savings', 'timestamp'
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        # Explicitly loop through collected data
        for user in users_data:
            writer.writerow(user)

# =============================================
# Flask Routes
# =============================================
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Validate required fields
            required_fields = ['name', 'age', 'email', 'gender', 'income']
            if not all(field in request.form for field in required_fields):
                raise ValueError("Missing required fields")

            # Create User instance
            user = User(
                name=request.form['name'],
                age=int(request.form['age']),
                email=request.form['email'],
                gender=request.form['gender'],
                income=float(request.form['income']),
                expenses={
                    'utilities': max(0, float(request.form.get('utilities', 0))),
                    'entertainment': max(0, float(request.form.get('entertainment', 0))),
                    'school_fees': max(0, float(request.form.get('school_fees', 0))),
                    'shopping': max(0, float(request.form.get('shopping', 0))),
                    'healthcare': max(0, float(request.form.get('healthcare', 0)))
                }
            )

            # Store in MongoDB
            result = users_collection.insert_one(user.to_dict())
            print(f"📝 Inserted document with id: {result.inserted_id}")

            # Save to CSV (wrapped in list to demonstrate looping)
            save_users_to_csv([user.to_dict()])

            return redirect(url_for('thank_you'))

        except ValueError as e:
            return render_template('index.html', error=f"Validation error: {str(e)}")
        except Exception as e:
            return render_template('index.html', error=f"An error occurred: {str(e)}")

    return render_template('index.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

# =============================================
# Custom Server Implementation
# =============================================
def run_server():
    port = 5000
    max_retries = 3
    retry_delay = 1
    
    for attempt in range(max_retries):
        try:
            print(f"🚀 Attempting to start server on port {port}...")
            run_simple(
                '0.0.0.0', 
                port,
                app,
                use_reloader=False,
                use_debugger=True,
                threaded=True
            )
            break
        except OSError as e:
            if e.winerror == 10038:  # Socket error
                print(f"⚠️ Port {port} unavailable, trying next port...")
                port += 1
                time.sleep(retry_delay)
            else:
                raise
    else:
        print(f"❌ Failed to start server after {max_retries} attempts")
        raise SystemExit("Could not find available port")

if __name__ == '__main__':
    run_server()