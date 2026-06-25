from fastapi import FastAPI
from pydantic import BaseModel
from database import create_table,add_teacher,get_teachers,add_course,get_courses,update_course,update_teacher,delete_course,delete_teacher

app = FastAPI()
create_table()

class Teacher(BaseModel):
    name:str
    id_number:int
    department:str
    email:str
    age:int

class Courses(BaseModel):
    course_trainer:str
    course_name:str
    department_name :str
    students_taking_the_course : int
    code:str

# students = []
teachers=[]
courses=[]

@app.get("/")
def home():
    return{"message": "Welcome to my API server"}


@app.get("/teachers")
def list_teachers():
    teachers=get_teachers()
    return teachers

@app.get("/courses")
def list_courses():
    courses=get_courses()
    return courses


def register_teacher(teacher: Teacher):
    add_teacher(teacher.name,teacher.id_number,teacher.department,teacher.email,teacher.age)
    return teacher

def register_course(course: Courses):
    add_course(course.course_trainer,course.course_name,course.department_name,course.students_taking_the_course,course.code)
    return course


@app.put("/teachers/{teacher_id}")
def edit_teacher(teacher_id: int, teacher: Teacher):
    update_teacher(teacher_id, teacher.name, teacher.id_number, teacher.department, teacher.email, teacher.age)
    return {"message": f"Teacher with ID {teacher_id} updated successfully", "teacher": teacher} 


@app.put("/courses/{course_id}")
def edit_course(course_id: int, course: Courses):
    update_course(course_id, course.course_trainer,course.course_name,course.department_name,course.students_taking_the_course,course.code)
    return {"message": f"course with ID {course_id} updated successfully", "course": course} 

@app.delete("/teachers/{teacher_id}")
def remove_teacher(teacher_id: int):
    """
    Deletes a teacher from the temporary database by their ID.
    """
    delete_teacher(teacher_id)
    return {"message": f"Teacher with ID {teacher_id} deleted successfully"}


@app.delete("/courses/{course_id}")
def remove_course(course_id: int):
    """
    Deletes a course from the temporary database by its ID.
    """
    delete_course(course_id)
    return {"message": f"Course with ID {course_id} deleted successfully"}


@app.post("/courses")
def create_courses(course: Courses):
    courses.append(course)
    return {"message": "Courses registered", "courses": course}

@app.post("/teachers")
def create_teacher(teacher: Teacher):
    teachers.append(teacher)
    return {"message": "Teacher registered", "teacher": teacher}






