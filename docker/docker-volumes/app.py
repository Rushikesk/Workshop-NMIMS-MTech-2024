from flask import Flask, request

app = Flask(__name__)

# EndPoint with @ decorator
@app.route("/")
def hello_world():
    f = open('./docker-data/message.txt', 'r')
    message = f.read()
    return  f'Hello , {message}'

if __name__== "__main__":
    # With app.run, you can directly run this as a python script
    app.run(host="0.0.0.0")

# Running the app
# RUNNING THE APP: python -m flask --app flask/lab1_quickstart.py run
# RUNNING APP OVER WEB: python -m flask --app flask/lab1_quickstart.py run --host=0.0.0.0
# GETTING DATA FROM JSON: curl http://127.0.0.1:5000/getname -H "Content-Type:application/json" -d '{"Name": "ajinkya"}'