from flask import Flask
from flask import request
app = Flask(__name__)


@app.route("/euler")  
def euler1():
    
    sum = 0
    for x in range (1,1000):
    
        if x%3 == 0 or x%5 == 0:
        
            sum +=x
    return (sum)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
