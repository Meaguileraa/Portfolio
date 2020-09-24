"""Server for portfolio."""

from flask import (Flask, render_template, jsonify, request, redirect)

app = Flask(__name__) 

@app.route("/")
def homepage():
    """View a homepage."""

    return render_template("root.html")



@app.route("/projects")
def projects_page():
    """View all projects."""

    return render_template("root.html")



@app.route("/resume")
def resume_page():
    """View resume."""
    #view or download resume? 

    return render_template("root.html")



@app.route("/contact")
def contact_page():
    """View listed contact information."""
    #linkedin, github, email, phone number

    return render_template("root.html")




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    #change to app.run() when complete 