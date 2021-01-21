"""Server for portfolio."""

from flask import (Flask, render_template, jsonify, request, redirect)
from jinja2 import StrictUndefined



"""Server for portfolio app."""
app = Flask(__name__) 
app.secret_key = "portfolio"
app.jinja_env.undefined = StrictUndefined



@app.route("/", methods = ["GET"])
def homepage():
    """View a homepage."""

    return render_template("homepage.html")

#resume, projects, contact info 




if __name__ == '__main__':
    # app.run()
    app.run(debug=True, host='0.0.0.0')
    #change to app.run() when complete 