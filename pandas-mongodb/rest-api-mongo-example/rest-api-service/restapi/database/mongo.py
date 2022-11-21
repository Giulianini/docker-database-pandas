import json
import os

import pymongo
from bson import json_util


class DBManager:
    def __init__(self):
        # Load configuration from environment variable.
        db_user = os.environ['user']
        db_pwd = os.environ['password']
        db_host = os.environ['host']
        db_port = os.environ['port']
        db_name = os.environ['database']

        # connection string
        self.mongo_client = pymongo.MongoClient(f"mongodb://{db_user}:{db_pwd}@{db_host}:{db_port}"
                                                f"/?authMechanism=DEFAULT")
        self.db = self.mongo_client[db_name]

        # connect to database
        print(f"Mongo dbs: {self.mongo_client.list_database_names()}")

    def add_course(self, course_id, university_id, name, max_students) -> bool:
        course_collection = self.db["course"]
        data_key = {"id": course_id}
        data = {"$set": {"id": course_id, "university_id": university_id, "name": name, "max_students": max_students}}
        x = course_collection.update_one(data_key, data, upsert=True)
        if x:
            print(f"Inserted id: {x}")
            return True
        else:
            return False

    def del_course(self, course_id) -> bool:
        course_collection = self.db["course"]
        data = {"id": course_id}
        affected_data = course_collection.delete_many(data).deleted_count
        if affected_data > 0:
            print(f"Affected data: {affected_data}")
            return True
        else:
            return False

    def add_student(self, student_id, course_id, name, surname, year):
        course_collection = self.db["student"]
        data_key = {"id": student_id}
        data = {"$set": {"id": student_id, "course_id": course_id, "name": name, "surname": surname}}
        x = course_collection.update_one(data_key, data, upsert=True).upserted_id
        if x:
            print(f"Inserted id: {x}")
            return True
        else:
            return False

    def del_student(self, course_id, student_id):
        course_collection = self.db["student"]
        data = {"id": student_id, "course_id": course_id}
        affected_data = course_collection.delete_many(data).deleted_count
        if affected_data > 0:
            print(f"Affected data: {affected_data}")
            return True
        else:
            return False

    def get_courses(self):
        course_collection = self.db["course"]
        courses = json_util.dumps(course_collection.find({}))
        return courses
