# app.py
from flask import Flask, g, render_template
from web_dao import WebDao

app = Flask(__name__)
DB_FILE = "C:\\work\\training\\python\\PythonAdvancedNovember2025\\testdb.db"

@app.teardown_appcontext
def close_db(error=None):
    print ("closing database")
    db = g.pop("db", None)
    if db is not None:
        db.close()

@app.get("/members")
def members():
    dao = WebDao(DB_FILE)
    members = dao.get_all()
    print (members)
    #return "<h1>Did this work?</h1>"
    return render_template("members.html", 
                           heading="Member List", 
                           members=members)





@app.get("/")
def home():

    title = "Professional Training Homepage"

    colours = ["red", "green", "blue"]
    return render_template(
        "index.html", 
        title=title, 
        colours=colours
    )

@app.get("/about")
def about():
    title="About Us"

    return render_template(
        "index.html", 
        title=title, #
        colours=[]
    )

if __name__ == "__main__":

    app.run(debug=True)
