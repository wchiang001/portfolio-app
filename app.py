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
                           year=2025,
                           links=[
                               {"url": "aboutme.html", "text": "About Me"},
                               {"url": "https://www.linkedin.com/in/nicholas-cww/", "text": "LinkedIn"},
                               {"url": "mycv.html", "text": "My CV"},
                               {"url": "myprojects.html", "text": "My Projects"},
                               {"url": "python_project.html", "text": "Python Project (WIP)"}
                           ])

if __name__ == "__main__":
    app.run(debug=True)
