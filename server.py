from flask import Flask, render_template, request
from comment import scrape
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/comment/', methods=['GET', 'POST'])
# def analyse():
#     url = request.args.get('param')
#     return scrape(url)


if __name__ == '__main__':
    app.run()
