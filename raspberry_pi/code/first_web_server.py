# first_web_server

from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    return "Hello, World!"

app.run(host="0.0.0.0" , port = 8080)

# to access web server outside of raspberry pi

# must be using same network as raspberry pi

#to find ip address of raspberry pi use command: hostname -I

#  use ip_address_of_raspberry_pi:8080 in web browser

# to stop the server use ctrl + C in terminal


