# web_dao.py

import sqlite3
from flask import g
from member_manager import MemberDao

class WebDao(MemberDao):
    def __init__(self, filename="./members.db"):
        self.filename = filename
        self.conn = self.get_connection()

    def get_connection(self):

        if "db" not in g:
            g.db = sqlite3.connect(self.filename, check_same_thread=False)
            g.db.execute("PRAGMA foreign_keys = ON;")
            g.db.execute("PRAGMA journal_mode = WAL;")
            g.db.execute("PRAGMA synchronous = NORMAL;")
            g.db.row_factory = sqlite3.Row  # For dict-like access
        return g.db
    
    def close(self):
        # Flask will close the database
        pass


