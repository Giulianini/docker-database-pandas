import dotenv

from mongo import DBManager
if __name__ == '__main__':
    dotenv.load_dotenv()
    db = DBManager()
    db.add_course(1, 1, "Algebra", 100)
    db.add_course(2, 1, "Analysis", 150)
    print(db.get_courses())
