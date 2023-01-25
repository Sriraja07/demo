from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def home():
    return "Sriraja B"

#app.run(debug=True)
