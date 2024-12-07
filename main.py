import threading
from flask import Flask, render_template
from telegram_bot import CPU, RAM, DISK, NETWORK, GENERAL_INFO
import app as main

app = Flask(__name__)

# Routing
@app.route("/", methods=["POST", "GET"])
def dashboard():
    disk_object = DISK.to_dict()
    return render_template("dashboard.html", cpu=CPU, ram=RAM, disk=disk_object, network=NETWORK, general=GENERAL_INFO)

@app.route("/settings", methods=["POST", "GET"])
def settings():
    return render_template("settings.html")

@app.route("/users", methods=["POST", "GET"])
def users():
    return render_template("users.html")

@app.route("/faq", methods=["POST", "GET"])
def faq():
    return render_template("faq.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")


def run_flask():
    app.run(debug=True, use_reloader=False)


if __name__ == "__main__":
    #app.run(debug=True)
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True  # Il thread Flask termina con il programma
    flask_thread.start()

    main.main()

