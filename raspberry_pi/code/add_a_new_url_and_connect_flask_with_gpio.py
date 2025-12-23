# add_a_new_url_and_connect_flask_with_gpio


from flask import Flask
import RPi.GPIO as GPIO

BUTTON_PIN = 26

app = Flask(__name__)

@app.route("/")

def index():
    return "Hello, World!"

@app.route("/push-button")

def checkpush_button_state():
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        return "Button is Pressed"
    
    else:
        return "Button is Not Pressed"
    

app.run(host="0.0.0.0" , port = 8080)
