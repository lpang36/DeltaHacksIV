from flask import Flask,request, Response, jsonify,abort
import json
import fastAStar


app = Flask(__name__)

app.config.update(JSONIFY_PRETTYPRINT_REGULAR=False)

@app.route('/api/<int:min_x>/<int:min_y>/<int:max_x>/<int:max_y>', methods = ['GET'])
def api(min_x,min_y,max_x,max_y):
    data = fastAStar.path(min_x,min_y,max_x,max_y)
    print(data)
    #var = [var for var in data if var['id']== choice]

    #if(len(var) == 0):
    #    abort(404)
    return jsonify({'path':data})


    """resp = jsonify(data)
    resp.status_code = 200
    return resp"""


if __name__ == "__main__":
    app.run()
