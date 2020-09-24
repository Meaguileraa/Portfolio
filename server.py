"""Server for portfolio."""

from flask import (Flask, render_template, jsonify, request, redirect)

app = Flask(__name__) 

@app.route('/')
def homepage():
    """View a homepage."""

@app.route('/projects')
def projects_page():
    """View all projects."""

@app.route('/resume')
def resume_page():
    """View resume."""
    #view or download resume? 

@app.route('/contact')
def contact_page():
    """View listed contact information."""
    #linkedin, github, email, phone number


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    #change to app.run() when complete 