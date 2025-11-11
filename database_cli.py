# database_cli.py


from member_dao import MemberDao

dao = MemberDao("member_database.db")

members = dao.get_all()

for member in members:
    print (member.name)

dao.close()