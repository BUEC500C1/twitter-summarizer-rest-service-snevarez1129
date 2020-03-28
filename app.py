from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/<handle>")
def api_call(handle):
    api = "http://3.81.205.114/" + str(handle)
    resp = requests.get(api) #call the api with the twitter handle
    print(resp.status_code)
    done = "done" #once video has been created load video
    return done

if __name__ == "__main__":
    app.run(debug=True)
