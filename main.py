from flask import Flask, render_template

app = Flask("app")

@app.route("/")
def hello_world():
  return render_template("dogs.html")

app.run(host='0.0.0.0', port=5000)
