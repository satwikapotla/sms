from flask import Flask, render_template,request,redirect,url_for
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

@app.route('/add', methods=['POST'])
def add():
    # Get data from the form
    name = request.form.get('name')
    age = request.form.get('age')
    course = request.form.get('course')

    # Create a new student instance
    new_student = student(name=name, age=age, course=course)

    # Add the new student to the database
    db.session.add(new_student)
    db.session.commit()

    # Optionally, redirect to the home page or render another template
    return redirect(url_for('home'))  # Redirect to the home page after adding

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    std = student.query.get_or_404(id)
    if request.method == 'POST':
        # Get updated data from the form
        std.name = request.form.get('name')
        std.age = request.form.get('age')
        std.course = request.form.get('course')
        # Commit changes to the database
        db.session.commit()
        # Redirect to the home page after updating
        return redirect(url_for('home'))
    # Render the edit form for GET requests
    return render_template('edit.html', student=std)

@app.route('/delete/<int:id>', methods=['GET'])
def delete_student(id):
    std = student.query.get_or_404(id)
    db.session.delete(std)
    db.session.commit()
    return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True)