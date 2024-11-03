from flask import Flask
app = Flask("__name__")



@app.route("/")
def welcome():
    return "Welcome to the Simple Flask App!"
@app.route("/index")
def infex():
    return "Welcome to the Index Flask App!"
@app.route("/html")
def html():
    return "Welcome to the Simple Flask App!"


if __name__ == "__main__":
    app.run(debug=True)  # Enable debugging mode

