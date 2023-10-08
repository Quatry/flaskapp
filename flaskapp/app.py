from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    course = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.id


@app.route('/')
def main_page():
    return render_template('mainpage.html')

@app.route('/create-student/', methods=['POST', 'GET'])
def add_page():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form['last_name']
        course = request.form['course']

        student = Student(first_name=first_name, last_name=last_name, course=course)

        try:
            db.session.add(student)
            db.session.commit()
            return redirect('/students/')
        except:
            return "При добавлении студента произошла ошибка"
    else:
        return render_template('addstudent.html')


@app.route('/students/')
def all_students():
    students = Student.query.order_by(Student.last_name).all()
    return render_template('students.html',students = students)

@app.route('/students/<int:id>/')
def about_student(id):
    student = Student.query.filter_by(id = id).all()
    print(student)
    return render_template('about_student.html', student = student)

if __name__ == '__main__':
    app.run(debug=True)
