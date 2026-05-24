from flask import Flask

app = Flsk(__name__)

@app.route('/')
def hello():
    return "Hello from Jenkins pipeline + Docker"

if __name__ == '__main__':
   app.run(host='0.0.0.0' , port=5000)