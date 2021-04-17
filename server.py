from flask import Flask, render_template
from comment import scrape
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/comment/<url>')
# def analyse(url):
#     scrape(url)
#     # if __name__ == '__main__':
#     #   app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
