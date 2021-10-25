from flask import *
from functions import userIP
from requests import get
import json

app = Flask(__name__)

@app.route('/')
def index():
    #<<<<<<<<<<<<<<<<<<<<<<<<------- initialNewdata
    data = userIP('0.0.0.0')
    newData = data.json()
    return render_template('index.html',newData=newData)

@app.route('/API', methods=['POST'])
def API():
    if request.method == 'POST':
        data = userIP(request.form['ipaddress'])
        newData = data.json()
    #<<<<<<<<<<<<<<<<<<<<<<<<------- newData handling html
        if 'error' in newData: 
            error = True
            reason = newData['reason']
            return render_template('index_error.html', error=error, reason=reason)
        else:
             return render_template('index.html',newData=newData)

if __name__ == '__main__':
    app.run(debug=True)