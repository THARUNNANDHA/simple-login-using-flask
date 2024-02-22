
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class login_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/add_data', methods=['POST'])
def add_data():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['uname']
        passw = request.form['psw']
        phone   = request.form['phone']

        existing_data = login_data.query.filter_by(name=name, password=passw).first()
        
        if existing_data:
            # If data exists, redirect to the welcome page
            return render_template('errorpage.html', name=name)
        else:
            new_data = login_data(name=name, password=passw,phone=phone)
            db.session.add(new_data)
        db.session.commit()
        
        
    
@app.route('/check_data', methods=['POST'])
def check_data():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['uname']
        passw = request.form['psw']
        admin_name='tharun'
        admin_password='Ntharun'

        # Check if the data already exists in the database
        existing_data = login_data.query.filter_by(name=name, password=passw).first()
        
        if admin_name==name and admin_password==passw:
            # If data exists, redirect to the welcome page
            return render_template('admin.html')
        elif existing_data:
            # If data does not exist, redirect to the login page
            return render_template('welcome.html', name=name)
        else:
            return render_template('signup.html')

@app.route('/delete_all', methods=['GET', 'POST'])
def delete_all():
    if request.method == 'POST':
        # Delete all rows from the login_data table
        db.session.query(login_data).delete()
        db.session.commit()
        
        return redirect(url_for('home'))


@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    # Create database tables before running the app
    with app.app_context():
        db.create_all()
    app.run(debug=True)

