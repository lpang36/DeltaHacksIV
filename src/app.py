from flask import Flask,request, Response, jsonify,abort, render_template
import json
from path_plan import path_plan


app = Flask(__name__)

app.config.update(JSONIFY_PRETTYPRINT_REGULAR=False)

@app.route('/')
def __main__():
  return render_template('index.html')

@app.route('/api/<min_x>/<min_y>/<max_x>/<max_y>', methods = ['GET'])
def api(min_x,min_y,max_x,max_y):
  data = path_plan((float(min_x),float(min_y)),(float(max_x),float(max_y)))
  print(data)
  return jsonify({'path':data})

if __name__ == "__main__":
  app.run()
