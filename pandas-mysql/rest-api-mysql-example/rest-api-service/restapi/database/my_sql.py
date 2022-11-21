import json
import os

import sqlalchemy
from pymysql import IntegrityError
from sqlalchemy import text
from sqlalchemy.engine import CursorResult
from sqlalchemy.exc import IntegrityError


class DBManager:
    def __init__(self):
        self.connection: sqlalchemy.engine.Connection
        # Load configuration from environment variable.
        db_user = os.environ['user']
        db_pwd = os.environ['password']
        db_host = os.environ['host']
        db_port = os.environ['port']
        db_name = os.environ['database']

        # connection string
        connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'

        # connect to database
        engine = sqlalchemy.create_engine(connection_str)
        self.connection = engine.connect()
        print(f"Connected: {not self.connection.closed}")
        metadata = sqlalchemy.MetaData(bind=engine)
        print(f"Metadata: {metadata}")

    def add_course(self, course_id, university_id, name, max_students) -> bool:
        query: str = text(
            """
                INSERT INTO course(course_id, university_id, name, max_students)
                VALUES (:course_id, :university_id, :name, :max_students)
            """)
        try:
            result: CursorResult = self.connection.execute(query,
                                                           {"course_id": course_id, "university_id": university_id,
                                                            "name": name,
                                                            "max_students": max_students})
            print(f"Affected lines: {result.rowcount}")
            return True
        except IntegrityError:
            return False

    def del_course(self, course_id) -> bool:
        query: str = text(
            """
               DELETE FROM course WHERE course_id= :course_id;
            """)
        try:
            result: CursorResult = self.connection.execute(query, {"course_id": course_id})
            print(f"Affected lines: {result.rowcount}")
            return True
        except IntegrityError:
            return False

    def add_student(self, student_id, course_id, name, surname, year):
        query: str = text(
            """
                INSERT INTO student(student_id, course_id, name, surname, year)
                VALUES (:student_id, :course_id, :name, :surname, :year)
            """)
        try:
            result: CursorResult = self.connection.execute(query, {"student_id": student_id, "course_id": course_id,
                                                                   "name": name, "surname": surname, "year": year})
            print(f"Affected lines: {result.rowcount}")
            return True
        except IntegrityError:
            return False

    def del_student(self, course_id, student_id):
        query: str = text(
            """
               DELETE FROM student WHERE student.course_id= :course_id AND student.student_id= :student_id;
            """)
        try:
            result: CursorResult = self.connection.execute(query, {"course_id": course_id, "student_id": student_id})
            print(f"Affected lines: {result.rowcount}")
            return True
        except IntegrityError:
            return False

    def get_courses(self):
        query: str = text(
            """
               SELECT * FROM course
            """)
        result = self.connection.execute(query).fetchall()
        return json.dumps([(dict(row.items())) for row in result])
