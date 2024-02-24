from flask import Flask, jsonify
from flask_mysqldb import MySQL
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ntharun@123'
app.config['MYSQL_DB'] = 'server'

mysql = MySQL(app)

# Function to add dummy data
def add_dummy_data():
    with app.app_context():
        cursor = mysql.connection.cursor()

        # Generate 10 sets of dummy data for today's date
        for _ in range(10):
            # Generate random emp_id (between 1 and 100) and shift (e.g., '8A', '8B', '8C')
            emp_id = random.randint(1, 100)
            shift = random.choice(['8A', '8B', '8C'])

            # Get today's date and time
            now = datetime.now()

            # Calculate random outtime as intime + random duration (between 1 and 4 hours)
            outtime = now + timedelta(hours=random.uniform(1, 4))

            # Execute SQL INSERT statement to add dummy data into the Attendance table
            cursor.execute('''
                INSERT INTO Attendance (emp_id, inTime, outTime, shiftType) VALUES (%s, %s, %s, %s)
            ''', (emp_id, now, outtime, shift))

        mysql.connection.commit()
        cursor.close()
        print("10 sets of data added for today's date.")

if __name__ == '__main__':
    add_dummy_data()
