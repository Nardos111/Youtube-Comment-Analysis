from re import sub
from flask import Flask, render_template, request, send_from_directory
from comment import scrape
import runapp
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


# @app.route('/video_info.csv', methods=['GET'])
# def serve_static2():
#     try:
#         return send_file('./video_info.csv',
#                          mimetype='csv',
#                          attachment_filename='video_info.csv',
#                          as_attachment=True)
#     except FileNotFoundError:
#         return ""


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
        # key = request.form['param']
        # data = key.split("/n")
        # ydict = {}
        # for i in range(len(data)):
        #     data[i] = data[i].split("|,")
        # with open("cleandata.csv", 'w', encoding="UTF8") as f:
        #     writer = csv.writer(f)
        #     writer.writerow(['number', 'comment', 'upvotes'])
        #     print(data)
        # for j in range(1, len(data)):
        #     ydict['number'] = data[j][0]
        #     ydict['comments'] = data[j][1]
        #     ydict['upvotes'] = data[j][2]
        #     writer.writerow(ydict.values())

        # for item in data:
        #     writer.writerow([item])
        # # writer.writerows(data)

        # return data_cleaning.cleanData(key)


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
