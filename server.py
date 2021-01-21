"""Server for portfolio."""

from flask import (Flask, render_template, jsonify, request, redirect)
# from model import connect_to_db
# import crud

from jinja2 import StrictUndefined



"""Server for portfolio app."""
app = Flask(__name__) 
app.secret_key = "portfolio"
app.jinja_env.undefined = StrictUndefined



@app.route("/", methods = ["GET"])
def homepage():
    """View a homepage."""

    return render_template("root.html")

#resume, projects, contact info 




if __name__ == '__main__':
    connect_to_db(app)
    # app.run()
    app.run(debug=True, host='0.0.0.0')
    #change to app.run() when complete 