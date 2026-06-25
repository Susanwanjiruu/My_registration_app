import sqlite3
from contextlib import contextmanager
sqlite_file_name = "school.db"
@contextmanager
def get_connection():
    connection = sqlite3.connect(sqlite_file_name)
    connection.row_factory=sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()

def create_table():
    with get_connection() as connection:
       
        
        connection.execute('''CREATE TABLE IF NOT EXISTS teachers(
                           teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           id_number INTEGER NOT NULL,
                           department TEXT NOT NULL,
                           email TEXT NOT NULL,
                           age INTEGER NOT NULL
                           )''')
        
        connection.execute('''CREATE TABLE IF NOT EXISTS courses(
                           course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           course_trainer TEXT NOT NULL,
                           course_name TEXT NOT NULL,
                           department_name TEXT NOT NULL,
                           students_taking_the_course INTEGER NOT NULL,
                           code TEXT NOT NULL
                           )''')
        


def add_teacher(name,id_number,department,email,age):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO teachers (name,id_number,department,email,age) VALUES (?,?,?,?,?)',(name,id_number,department,email,age)
        )

def update_teacher(teacher_id, name, id_number, department, email, age):
    with get_connection() as connection:
        connection.execute(
            'UPDATE teachers SET name=?, id_number=?, department=?, email=?, age=? WHERE teacher_id=?',
            (name, id_number, department, email, age, teacher_id)
        )

def delete_teacher(teacher_id):
    with get_connection() as connection:
        connection.execute('DELETE FROM teachers WHERE teacher_id=?', (teacher_id,))


def add_course(course_trainer,course_name,department_name,students_taking_the_course,code):
     with get_connection() as connection:
        connection.execute(
            'INSERT INTO courses (course_trainer,course_name,department_name,students_taking_the_course,code) VALUES (?,?,?,?,?)',(course_trainer,course_name,department_name,students_taking_the_course,code)
        )


def update_course(course_id, course_trainer, course_name, department_name, students_taking_the_course, code):
    with get_connection() as connection:
        connection.execute(
            'UPDATE courses SET course_trainer=?, course_name=?, department_name=?, students_taking_the_course=?, code=? WHERE course_id=?',
            (course_trainer, course_name, department_name, students_taking_the_course, code, course_id)
        )

def delete_course(course_id):
    with get_connection() as connection:
        connection.execute('DELETE FROM courses WHERE course_id=?', (course_id,))



def get_teachers():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM teachers').fetchall()

def get_courses():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM courses').fetchall()

