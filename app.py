from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/<handle>")
def api_call(handle):
    resp = handle
    return resp


if __name__ == "__main__":
    app.run(debug=True)
