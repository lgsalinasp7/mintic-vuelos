from flask import Flask
from flask import render_template as render
from flask import redirect
from flask import request


app =Flask(__name__)

Lista_usuarios=["Luis","Pedro","Daniel"] 
citas_medicas={
    "001": "cita 001",
    "002": "cita 002",
    "003": "cita 003",
}

sesion_iniciada= False


@app.route("/", methods=["GET"])
@app.route("/inicio", methods=["GET"])
def inicio():
    return render("inicio.html", sesion_iniciada=sesion_iniciada)

@app.route("/Registro", methods=["GET", "POST"])
def registro():
    return "pagina Registro"


@app.route("/ingreso", methods=[ "GET", "POST"])
def ingreso():
   global sesion_iniciada
   if request.method =="GET":
       return render("ingreso.html") 
   else:
       sesion_iniciada= True
       return render("/index.html")

@app.route("/salir", methods=["POST"])
def salir():
    global sesion_iniciada
    sesion_iniciada =False

    return redirect("/inicio")

@app.route("/index", methods=["GET","POST"])
def indexr():
    global sesion_iniciada
    sesion_iniciada =True

    return render("/index.html")

@app.route("/usuario/<id_usuario>", methods=["GET","POST"])
def usuario(id_usuario):
    if id_usuario in Lista_usuarios:
    
       return f"Estas Viendo el Perfil del Usuario:{id_usuario}"
    else:

       return f"Error El Usuario:{id_usuario} no existe"

@app.route("/crear_vuelos", methods=["GET", "POST"])
def crear_vuelos():
    return "pagina crear Vuelos"


@app.route("/vuelos/<id_vuelo>", methods=["GET" ])
def vuelos(id_vuelo):
    try:
        id_vuelo=int(id_vuelo)
    except Exception as e:
        id_vuelo = 0     
    if id_vuelo in vuelos:
    
       return f"Estas viendo El Vuelo:{id_vuelo}"
    else:

       return f"Error de Vuelo:{id_vuelo} no existe" 
    return "Solicitar_cita_usuario: {id_cita}"

@app.route("/calificar_vuelo", methods=["GET", "POST"])
def calificar_vuelo():
    return "pagina calificar  Vuelo"

if __name__=="__main__":
    app.run(debug=True)
