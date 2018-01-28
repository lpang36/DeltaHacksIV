from flask import Flask,request, Response, jsonify,abort
import json
import fastAStar
from path_plan import path_plan


app = Flask(__name__)

app.config.update(JSONIFY_PRETTYPRINT_REGULAR=False)

@app.route('/api/<min_x>/<min_y>/<max_x>/<max_y>', methods = ['GET'])
def api(min_x,min_y,max_x,max_y):
    data = path_plan((float(min_x),float(min_y)),(float(max_x),float(max_y)))
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
