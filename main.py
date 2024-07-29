from flask import Flask, render_template, request, redirect
import requests
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app=Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
with app.app_context():
    class User(UserMixin, db.Model):
        id = db.Column(db.Integer, primary_key=True)
        password = db.Column(db.String(100))
        name = db.Column(db.String(1000))




    db.create_all()
class MyModelView(ModelView):
    def is_accessible(self):
            return True

admin = Admin(app)
admin.add_view(MyModelView(User, db.session))



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login",methods=["POST","GET"])
def login():
        if request.method == "POST":
         name = request.form.get("name")
         password = request.form.get("password")

         return redirect("/index.html")

         return render_template("login.html")


app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")

        new_user = User(
            name=name,
            password=password,
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")


if __name__=="__main__":
    app.run(debug=True)