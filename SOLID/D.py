# 5.  dependency inversion principle
# High-level modules should not depend on low-level modules.
from abc import ABC, abstractmethod
import random


class DBInterface(ABC):

    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def get(self, id):
        pass


class SQLdb(DBInterface):

    def insert(self, data):
        print(f"inserted {data} from mysql")
        return random.randint(0, 100)

    def get(self, id):
        print(f"get user {id} data from mysql")
        return {'id': id, "data": "some_data"}


class Mongodb(DBInterface):

    def insert(self, data):
        print(f"inserted {data} from mongo")
        return random.randint(0, 100)

    def get(self, id):
        print(f"get user {id} data from mongo")
        return {'id': id, "data": "some_data"}


class Blog:

    def __init__(self, db, blog_id):
        self.db = db
        self.blog_id = blog_id

    def add_user(self, name):
        self.db.insert(name)

    def get_users(self):
        return self.db.get(self.blog_id)


if __name__ == '__main__':
    sql_db = SQLdb()
    mongo_db = Mongodb()

    blog_with_sql = Blog(db=sql_db, blog_id=1)
    blog_with_sql.add_user("test")

    blog_with_mongo = Blog(db=mongo_db, blog_id=1)
    blog_with_mongo.add_user("test")
