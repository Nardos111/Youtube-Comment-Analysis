from flask import Flask, render_template, request
from comment import scrape
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/comment/', methods=['GET', 'POST'])
def analyse():
    if request.method == "POST":
        try:
            key = request.form['keyword']
            return scrape(key)
        except:
            return "Can't access video"


if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

if __name__ == '__main__':
    app.run()
