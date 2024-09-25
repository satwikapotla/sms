from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#initialize flask
app = Flask(__name__)

# MySQL configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin123@localhost/student_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    course = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Student {self.name}, Age: {self.age}, Course: {self.course}>'
# Define routes
@app.route('/')
def home():
    students = student.query.all()  # Fetch all students from the database
    return render_template('index.html', students=students)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)