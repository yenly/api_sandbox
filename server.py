from flask import Flask, render_template
from jinja2 import StrictUndefined

app = Flask(__name__)

@app.route('/')
def index():
    """Display list of APIs"""

    return render_template('index.html')


if __name__ == "__main__":
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    
    app.run(host="0.0.0.0")
