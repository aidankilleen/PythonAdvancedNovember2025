# app.py


from flask import Flask, render_template


app = Flask(__name__)


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
