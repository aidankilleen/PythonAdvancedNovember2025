# test_member_dao.py


import sqlite3
import pytest
from Member import Member
from member_dao import MemberDao

def test_open_close():

    dao = MemberDao()
    dao.close()


def test_get_all():
    dao = MemberDao()
    members = dao.get_all()
    assert(len(members)) > 0
    dao.close()


def test_insert_delete():
    member = Member(-1, "New User", "new.user3@gmail.com", True)
    dao = MemberDao()
    added_member = dao.add(member)
    dao.delete(added_member.id)
    dao.close()

    assert added_member.id != -1

def test_duplicate_email_fails():

    dao = MemberDao()
    m1 = Member(-1, "Aidan", "abcde@gmail.com", True)
    m2 = Member(-1, "Alice", "abcde@gmail.com", False)

    m1 = dao.add(m1)

    # verify that this causes an exception
    with pytest.raises(sqlite3.IntegrityError):
        dao.add(m2)

    dao.delete(m1.id)
    dao.close()

