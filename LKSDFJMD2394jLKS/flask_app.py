
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template

import pandas as pd
import joblib

app = Flask(__name__, template_folder='/home/j578666/mysite/', static_folder='/home/j578666/mysite/static/')





@app.route('/', methods=['GET', 'POST'])
#def hello_world():
#    return 'Hello from Flask!~~~~'


def load():
    clf = joblib.load("/home/j578666/mysite/regr.pkl")

    if request.method == "POST":
        age = request.form.get("age")
        weight = request.form.get("weight")
        x = pd.DataFrame([[age, weight]], columns=["Age", "Weight"])
        output = clf.predict(x)[0]
        #print(prediction)
        return render_template("HW2.html", output=output)

    return render_template("HW2.html")




