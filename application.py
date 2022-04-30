from flask import Flask, render_template, request

my_first_app = Flask(__name__)


@my_first_app.route("/")
def index():
    return render_template("index.html")

@my_first_app.route("/hello", methods=["POST"])
def login():
    name=request.form.get("nombre")
    apellido=request.form.get("apellido")
    cumple=request.form.get("cumple")
    email=request.form.get("email")
    numero=request.form.get("numero")
    sexo=request.form.get("sexo")
    pais=request.form.get("pais")
    return render_template("session.html", name=name, apellido=apellido, cumple=cumple, email=email, numero=numero,sexo=sexo,pais=pais)


@my_first_app.route("/<string:name>")
def session(name):
    return render_template("session.html", name=name)


@my_first_app.route("/users")
def names():
    # query a data base for users
    name_list=["jose", "pedro","maria"]
    return render_template("list.html",nombres=name_list)
    
