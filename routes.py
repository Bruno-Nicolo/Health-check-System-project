from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from telegram_bot import CPU, RAM, DISK, NETWORK, GENERAL_INFO
from main import BOT
from user import User

def register_routes(app, db, bcrypt):

    @app.route("/", methods=["POST", "GET"])
    def dashboard():
        if current_user.is_authenticated:
            disk_object = DISK.to_dict()
            return render_template("dashboard.html", cpu=CPU, ram=RAM, disk=disk_object, network=NETWORK,
                                   general=GENERAL_INFO)
        else:
            return render_template("login.html", result="")


    @app.route("/settings", methods=["POST", "GET"])
    def settings():
        user = db.session.query(User).get(current_user.id)
        if request.method == "GET":
            return render_template("settings.html", cpu=user.settings["cpu"], ram=user.settings["ram"], disk=user.settings["disk"],
                                   temperature=user.settings["temperature"], interval=BOT.interval)
        if request.method == "POST":

            if request.form.get("cpu") != "":
                value = int(request.form.get("cpu"))
                CPU.set_threshold(value)

            if request.form.get("ram") != "":
                value = int(request.form.get("ram"))
                RAM.set_threshold(value)

            if request.form.get("disk") != "":
                value = int(request.form.get("disk"))
                DISK.set_threshold(value)

            if request.form.get("temperature") != "":
                value = int(request.form.get("temperature"))
                GENERAL_INFO.set_threshold(value)

            if request.form.get("interval") != "":
                value = int(request.form.get("interval"))
                BOT.set_interval(value)

            try:
                updated_settings = user.settings.copy()
                updated_settings["cpu"] = CPU.threshold
                updated_settings["ram"] = RAM.threshold
                updated_settings["disk"] = DISK.threshold
                updated_settings["temperature"] = GENERAL_INFO.threshold

                user.settings = updated_settings

                user.interval = BOT.interval

                db.session.add(user)
                db.session.commit()

                return redirect(url_for("settings"))
            except Exception as e:
                db.session.rollback()
                return f'Errore durante l\'aggiornamento: {e}'




    @app.route("/users", methods=["POST", "GET", "DELETE"])
    def users():
        user = db.session.query(User).get(current_user.id)
        if user.chat_id is None:
            user.chat_id = []

        if request.method == "GET":
            return render_template("users.html", chat_list=user.chat_id)
        if request.method == "POST":

            if "add_item" in request.form:
                new_item = f"{request.form.get('item')}"
                if new_item not in user.chat_id:
                    updated_list = current_user.chat_id + [new_item]
                    user.chat_id = updated_list

                    BOT.update_id_list(updated_list)

                    db.session.add(user)
                    db.session.commit()
                    return redirect(url_for("users"))

            elif "delete_item" in request.form:
                item_to_delete = request.form.get("delete_item")

                updated_list = [item for item in user.chat_id if item != item_to_delete]
                user.chat_id = updated_list

                BOT.update_id_list(updated_list)

                db.session.add(user)
                db.session.commit()

                return redirect(url_for("users"))


    @app.route("/faq")
    def faq():
        return render_template("faq.html")


    @app.route("/register", methods=["POST", "GET"])
    def register():
        if request.method == "GET":
            return render_template("register.html")
        elif request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")

            hashed_password = bcrypt.generate_password_hash(password)

            new_user = User(username=username, password=hashed_password)

            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("dashboard"))


    @app.route("/login", methods=["POST", "GET"])
    def login():
        if request.method == "GET":
            return render_template("login.html")
        elif request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")

            try:
                user = User.query.filter(User.username == username).first()

                print(bcrypt.check_password_hash(user.password, password))

                if bcrypt.check_password_hash(user.password, password):
                    login_user(user)

                    #BOT.update_id_list(user.chat_id)

                    #print(type(user.settings["cpu"]))
                    #print(type(CPU.threshold))
                    #CPU.set_threshold(user.settings["cpu"])
                    #RAM.set_threshold(float(user.settings["ram"]))
                    #DISK.set_threshold(float(user.settings["disk"]))
                    #GENERAL_INFO.set_threshold(float(user.settings["temperature"]))
                    return redirect(url_for("dashboard"))
                else:
                    return render_template("login.html", result="failed")
            except Exception as e:
                #return render_template("login.html", result="failed")
                return f"{e}"


    @app.route("/logout", methods=["POST", "GET"])
    def logout():
        logout_user()
        BOT.update_id_list("")
        return render_template("login.html")
