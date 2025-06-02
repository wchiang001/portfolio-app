from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",
                           title="Nicholas' Portfolio",
                           header_text="Getting to Know Me",
                           name="Nicholas Chiang",
                           tagline="Always a Work-In-Progress | Passion in Numbers | Relentless Learner",
                           contact_info="(+65)90188204 | wen_wei_91@hotmail.com",
                           email="wen_wei_91@hotmail.com",
                           year=2025)

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

@app.route("/credits")
def credits():
    return render_template("credits.html")

@app.route("/mycv")
def mycv():
    return render_template("mycv.html")

@app.route("/myprojects")
def myprojects():
    return render_template("myprojects.html")

@app.route("/python_project")
def python_project():
    return render_template("python_project.html")

if __name__ == "__main__":
    app.run(debug=True)
