from flask import Flask, render_template
from flask_flatpages import FlatPages
import json

# auto-reload wen page changes; look for .md files
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.md'

# Create our app object, use this page as our settings (will pick up DEBUG)
app = Flask(__name__)

# For settings we use this file itself, very easy to configure
app.config.from_object(__name__)

# We want Flask to allow no slashes after paths, bc they get turned into flat files
app.url_map.strict_slashes = False

# instance the static site
pages = FlatPages(app)

# Route to FlatPages @ root url; route any '.html' path
@app.route("/")
@app.route("/<path:path>.html")
def page(path=None):
    # look w FlatPages, or use "index" if no path
    page = pages.get_or_404(path or 'index')
    # render "page.html" w its metadata
    # with open("merged.combey.csv") as f:
    #     leet = json.load(f)
    return render_template("page.html", 
                                    page=page, 
                                    title=page.meta['title'])