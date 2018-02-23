from flask import Flask, request, jsonify
from tag import generateTags, test

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to report-tagging"


@app.route('/reportTagging', methods=['GET'])
def reportTag():
    if request.method == 'GET':
        r = request.args.get('report')
        tags = generateTags(r)
        return jsonify(tags)

if __name__ == '__main__':
    app.run(debug=True)
