from flask import Flask

# Create our app object, use this page as our settings (will pick up DEBUG)
app = Flask(__name__)

# For settings we use this file itself, very easy to configure
app.config.from_object(__name__)

# We want Flask to allow no slashes after paths, bc they get turned into flat files
app.url_map.strict_slashes = False

# Creates route to our index page at root url, returns simple greeting
@app.route("/")
def index():
    return "Hello, June 🐞"