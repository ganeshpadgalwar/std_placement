# Its main file
# responce code "GET / HTTP/1.1" 200 means our flask working fine

from flask import Flask , render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")




if __name__ == "__main__":
    app.run( debug= True, host="0.0.0.0",port=8080 )
     