from flask import Flask, redirect, url_for, render_template, request, session, flash


app = Flask(__name__)
app.config['SECRET_KEY'] = "MrWarcrime"


@app.route("/")
@app.route("/Home")
def Home():
    return render_template("Home.html")

@app.route("/Bush")
def BushElected():
    return render_template("BushElection.html")


@app.route("/Survivor")
def Survivor():
    return render_template("Survivor.html")

@app.route("/LotR")
def Lord_of_the_Rings():
    return render_template("Lord-of-the-Rings.html")

@app.route("/9-11")
def Nine11():
    return render_template("9-11.html")

@app.route("/PatAct")
def PatAct():
    return render_template("PatAct.html")

@app.route("/FBLaunch")
def FBLaunch():
    return render_template("Facebook.html")

@app.route("/IPhone")
def IPhone():
    return render_template("Iphone.html")

@app.route("/Obama")
def Obama():
    return render_template("ObamaElected.html")

@app.route("/Art")
def Art():
    return render_template("Art.html")

@app.route("/Music")
def Music():
    return render_template("Music.html")

@app.route("/Celebs")
def Celebs():
    return render_template("Celebs.html")

@app.route("/Fashion")
def Fashion():
    return render_template("Fashion.html")



if __name__ == "__main__":
    app.run()