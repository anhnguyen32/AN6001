from flask import Flask
from flask import render_template,request

app = Flask(__name__)
@app.route("/",methods=['GET','POST']) 
def index():
    return (render_template("index.html")) #backend

@app.route("/",methods=['GET','POST']) 
def main():
    name = request.form.get("q")
    return (render_template("main.html"))

if __name__ == "__main__": #confirm 
    app.run()

