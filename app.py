from flask import Flask, redirect, render_template, url_for, request, send_file
from bs4 import BeautifulSoup
import requests as req

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        myHandle = request.form["myHandle"]
        api = "http://54.152.189.151/" + str(myHandle)
        resp = req.get(api, stream=True)
        file_name = str(myHandle) + "_twitter_feed.mp4"
        with open(file_name, 'wb') as f:
            for chunk in resp.iter_content(chunk_size=1024*1024):
                if chunk:
                    f.write(chunk)
        return send_file(file_name)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
