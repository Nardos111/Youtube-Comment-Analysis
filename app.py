from operator import ge
from re import sub
from flask import Flask, render_template, request, send_from_directory
from comment import scrape
import runapp
import test
import generatewc
import csv
from wordcloud import WordCloud


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/output_scraping.csv', methods=['GET'])
def serve_static():
    try:
        return send_from_directory('./',
                                   'output_scraping.csv',
                                   as_attachment=True)
    except FileNotFoundError:
        return ""


@app.route('/video_info.csv/', methods=['GET'])
def serve_static2():
    try:
        return send_from_directory('./', 'video_info.csv')
    except FileNotFoundError:
        return ""


@app.route('/comment/', methods=['GET', 'POST'])
def analyse():
    if request.method == "POST":
        try:
            key = request.form['keyword']
            return scrape(key)
        except:
            return "Can't access video"


@app.route('/clean/', methods=['GET', 'POST'])
def cleanData():
    if request.method == "POST":
        return runapp.run()


@app.route('/analyze/', methods=['POST'])
def analyze():
    if request.method == "POST":
        return generatewc.generatewc()


if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

if __name__ == '__main__':
    app.run()


# @app.after_request
# def add_header(response):
#     response.cache_control.max_age = 300
#     return response
