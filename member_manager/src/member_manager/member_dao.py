# member_dao.py

# data access object for reading and writing to member database
import sqlite3
from dataclasses import dataclass

from .member import Member

@dataclass
class MemberDao():
    """MemberDao 
    class for reading and writing Member objects to the database
    Specify the filename or use the default
    Use create_schema to create the table
    make sure to call .close() when finished

    """
    filename: str

    def __init__(self, filename="member_database.db"):
        self.filename = filename
        self.conn = sqlite3.connect(self.filename)
    
    def get_all(self)->list[Member]:
        """get_all() returns all member objects as a list"""
        members:list[Member] = []
        cursor = self.conn.cursor()
        sql = "SELECT * FROM members"
        rs = cursor.execute(sql)

        for row in rs:
            (id, name, email, active) = row
            member = Member(id, name, email, active)

            members.append(member)
        return members
    def add_original(self, member):
        """DO NOT USE"""
        sql = f"""INSERT INTO members 
                (name, email, active) 
                VALUES(
                    '{member.name}', 
                    '{member.email}', 
                    {1 if member.active else 0}
                )"""
        cursor = self.conn.cursor()
        cursor.execute(sql, (1,))
        self.conn.commit()

        # read the newly generated id from the db
        member.id = cursor.lastrowid
        return member
    
    def add(self, member):
        """Insert a new record. NB: id will be ignored and assigned by the database"""
        sql = f"""INSERT INTO members 
                (name, email, active) 
                VALUES(?, ?, ?)"""
        cursor = self.conn.cursor()
        cursor.execute(sql, (member.name, member.email, member.active))
        self.conn.commit()

        # read the newly generated id from the db
        member.id = cursor.lastrowid
        return member

    def delete(self, id):
        """
        Delete a member record

        Args:
            id:int - the id to be deleted

        Returns:
            int: number of rows affected, 0 if id not found
        """
        sql = f"""DELETE FROM members WHERE id = {id}"""
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()

        return cursor.rowcount
        
    def update(self, member):
        """ Update a member
        
        record with member.id will be updated
        """
        try:
            sql = f"""UPDATE members 
                SET 
                    name = ?, 
                    email= ?, 
                    active= ? 
                WHERE id = ?"""
            cursor = self.conn.cursor()
            cursor.execute(sql, (member.name, member.email, member.active, member.id))
            self.conn.commit()
        except sqlite3.IntegrityError:
            # user with this email already exists
            raise ValueError("User with this email already exists")


    def close(self):
        """ Close the database. NB: close database when finished"""
        self.conn.close()

    def create_schema(self):
        """ create all tables in the database"""
        sql = """
                CREATE TABLE IF NOT EXISTS members (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    active BOOLEAN NOT NULL
                );
                """
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()



if __name__ == "__main__":

    dao = MemberDao()
    members = dao.get_all()

    for member in members:
        print (member)




