from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    msg = ""
    if request.method == "POST":
        name = request.form["name"]
        db = mysql.connector.connect(
            host="db",
            user="flaskuser",
            password="flaskpass",
            database="flaskdb"
        )
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        db.commit()
        msg = "Data saved!"
    return render_template("index.html", msg=msg)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

