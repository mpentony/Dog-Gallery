from flask import Flask, render_template, request

import requests

from dog_breeds import prettify_dog_breed


#main.py, dog_breeds.py are files  used to create a web app that allows users to select a dog breed and a number of images to display.
#In static folder, there is dogs.css used to style the web app.
#In templates folder, there is dogs.html used to create the web app.


app = Flask("app")

def check_breed(breed):
  return "/".join(breed.split("-"))

@app.route("/", methods=["GET","POST"])
def dog_image_gallery():
  errors = []
  if request.method == "POST":
    breed = request.form.get("breed")
    number = request.form.get("number")
    if not breed:
      errors.append("Oops! Please choose a breed.")
    if not number:
      errors.append("Oops! Please choose a number.")
    if breed and number:
      response = requests.get("https://dog.ceo/api/breed/" + check_breed(breed) + "/images/random/" + number)
      data = response.json()
      dog_images = data["message"]
      return render_template("dogs.html", images=dog_images, breed=prettify_dog_breed(breed), errors=[])
  return render_template("dogs.html", images=[], breed="", errors=errors)

@app.route("/random", methods=["POST"])
def get_random_dog():
  response = requests.get("https://dog.ceo/api/breeds/image/random")
  data = response.json()
  dog_image = data["message"]
  return render_template("dogs.html", images=[dog_image], breed="Random", errors=[])
  

app.debug = True
app.run(host='0.0.0.0', port=8080)
