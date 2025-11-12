# daomod_investigation.py
from member_manager import MemberDao, Member

dao = MemberDao("C:\\work\\training\\python\\PythonAdvancedNovember2025\\testdb.db")
dao.create_schema()

m = Member(-1, "Alice", "alice@gmail.com", True)

m = dao.add(m)


members = dao.get_all()

for member in members:
    print (member)

dao.close()