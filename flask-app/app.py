from flask import Flask
import  json

app = Flask(__name__)


@app.route('/')
def home():
    data = json.dumps({
        'sucess': True, 'msg': 'succesful'
    })
    return data

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)