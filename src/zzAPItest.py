from flask import Flask,request, Response, jsonify,abort
import json

app = Flask(__name__)

@app.route('/api/<int:choice>', methods = ['GET'])
def api(choice):
    data = [
        {
            'hello':'world','number':3,'id':0
        },
        {
            'hello' : 'goodmorning',
            'number' : 11,
            'id' : 1
        }
    ]

    var = [var for var in data if var['id']== choice]

    if(len(var) == 0):
        abort(404)
    return jsonify({'data':var[0]})


    """resp = jsonify(data)
    resp.status_code = 200
    return resp"""


if __name__ == "__main__":
    app.run()
