# member_dao.py

# data access object for reading and writing to member database
import sqlite3
from dataclasses import dataclass

from Member import Member


@dataclass
class MemberDao():
    filename: str =  "member_database.db"

    def __init__(self):
        self.conn = sqlite3.connect(self.filename)
    
    def get_all(self)->list[Member]:
        members:list[Member] = []
        cursor = self.conn.cursor()
        sql = "SELECT * FROM members"
        rs = cursor.execute(sql)

        for row in rs:
            id = row[0]
            name=row[1]
            email=row[2]
            active=row[3]
            member = Member(id, name, email, active)

            members.append(member)
        return members

if __name__ == "__main__":

    dao = MemberDao()
    members = dao.get_all()

    for member in members:
        print (member)




