# Its main file
# responce code "GET / HTTP/1.1" 200 means our flask working fine
from flask import Flask , render_template, request

import pickle
model = pickle.load(open("std_model.pkl","rb"))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route( "/predict", methods=["POST","GET"]) 
def student():
    cgpa_var = request.form.get("cgpa")
    iq_var = int(request.form.get("iq"))
    profile_score_var = int(request.form.get("profile_score"))
    result = model.predict([[cgpa_var, iq_var, profile_score_var]])
    print(result[0])
    print(cgpa_var)

    if result[0] == 1:
        final_result = "student is placed"
    else :
        final_result = "student is not placed"

    return render_template("index.html", prediction = final_result)



if __name__ == "__main__":
    app.run( debug= True, host="0.0.0.0",port=8080 )
     