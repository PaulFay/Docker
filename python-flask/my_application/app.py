from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/ok")
def hello():
    return "Hello Okeanus!"
  
@app.route("/hello")
def hello():
    return "Hello Everyone!"


@app.route("/sol1")
def e1():
    n = 0
    for i in xrange(1,1000):
       if not i % 5 or not i % 3:
             n = n + i
    print (n)
    return "Complete"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
