from flask import Flask, request, render_template, jsonify
import json


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def comment():
    swear = ['fuck', 'shit']
    rq = request.form['comments'].lower()
    for word in swear:
        if word in rq:
            return 'Bad Comment'
        return 'Comment posted'

if __name__ == '__main__':
    app.run()