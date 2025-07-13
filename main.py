from flask import Flask, render_template, request

import requests

app = Flask("app")

#function adds a dash in between breed names with multiple words like miniature poodle
def check_breed(breed):
  return "/".join(breed.split("-"))

@app.route("/", methods=["GET", "POST"])
def dog_image_gallery():
  errors=[]
  if request.method == "POST":
    breed=request.form.get("breed")
  return render_template("dogs.html")

app.debug = True

app.debug = True
app.run(host='0.0.0.0', port=5000)