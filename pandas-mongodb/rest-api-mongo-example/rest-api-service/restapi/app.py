import sys
import os

from dotenv import load_dotenv
from flask import Flask, request

sys.path.append("")
from database import mongo

# If outside a docker container load manually the configuration from .env file.
# If inside docker.env is passed to docker-compose
if os.environ["mode"] != "DOCKER":
    load_dotenv()

db_manager = mongo.DBManager()
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world"


@app.route("/add-course", methods=["PUT"])
def add_course():
    data = request.get_json()
    course_id = data["id"]
    name = data["name"]
    max_students = data["max_students"]
    res = db_manager.add_course(course_id=course_id, university_id=1, name=name, max_students=max_students)
    if res:
        return '', 201
    else:
        return 'Error adding course', 400


@app.route("/del-course", methods=["DELETE"])
def del_course():
    data = request.get_json()
    course_id = data["id"]
    res = db_manager.del_course(course_id=course_id)
    if res:
        return '', 200
    else:
        return f'Cannot find the course with id {course_id}', 404


@app.route("/add-student", methods=["PUT"])
def add_student():
    data = request.get_json()
    course_id = data["course_id"]
    student_id = data["student_card_id"]
    name = data["student_name"]
    surname = data["student_surname"]
    year = data["student_year"]
    res = db_manager.add_student(student_id=student_id, course_id=course_id, name=name, surname=surname, year=year)
    if res:
        return '', 201
    else:
        return 'Error adding student', 400


@app.route("/del-student", methods=["DELETE"])
def del_student():
    data = request.get_json()
    course_id = data["course_id"]
    student_id = data["student_card_id"]
    res = db_manager.del_student(course_id=course_id, student_id=student_id)
    if res:
        return '', 200
    else:
        return f'Cannot find the course with id {course_id}', 404


@app.route("/courses", methods=["GET"])
def get_courses():
    return db_manager.get_courses()
