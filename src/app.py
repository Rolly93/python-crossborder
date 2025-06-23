import secrets
from flask import Flask, render_template, request, redirect,send_from_directory ,flash , url_for
secrets.token_hex(16)


app = Flask(__name__)
app.secret_key = 'dev'
shipments_data =[]
dbnewUser = []


shipment ={
        'embarque':'',
        'tipoOperacion':'',
        'trailer':'',
        'referencia':'',
        'sello':'',
        'unidad':'',
        'cliente':'',
        'origen':'',
        'destino':'',
        'recoleccion':'',
        'salida':'',
        'inspeccion_rojo':'',
        'sello_mex':'',
        'verde_mex':'',
        'inspeccion_usa':'',
        'tipo_inspeccion':'',
        'sello_usa':'',
        'verde_usa':'',
        'resguardo':'',
        'patio':'',
        'recibe':'',
    }

@app.route("/")
def index():
    return redirect("login")

@app.route("/favicon.ico")
def  favicon():
    return send_from_directory(app.root_path,'static/example.ico',mimetype = 'example.ico')

@app.route('/login' , methods = ['GET','Post']) 
def login():    
    username = None
    password = None    
    if request.method == "GET":
        username = request.args.get('email')
        password = request.args.get('password')
        if username and password:
            if str(username).lower() =="rolando":
                return render_template("sft.html")
            else:
        
                print(username, password)
                
                return redirect("bordercross")
    return render_template("login.html")

@app.route('/newuser' , methods = ['GET'])
def newUser():
    if request.method == 'GET':# any to change it to 'POST'
        user = request.args        
        # Validacion  de constraseña
        success , error = _LogginVerification(user)

        if  success:
            flash("User created successfully!!")
            return redirect(url_for('login'))
        else: 
            flash(error)
            return render_template("newuser.html")
    return render_template("newuser.html")

def _LogginVerification(user):
    password = user.get("password")

    confirm_password = user.get("confirm_password")
    valid = False

    if not password or not confirm_password:
        valid = False, "Password fields are required."
        return valid

    if len(password) < 8:
        
        valid = False,"Password must be at least 8 characters long."
        return valid  

    if not any(char.isdigit() for char in password):
        valid = False, "Password must contain at least one number."
        return valid

    if not any(char.isupper() for char in password):
        valid = False, "Password must contain at least one uppercase letter."
        return valid

    if not any(char.islower() for char in password):
        
        valid = False, "Password must contain at least one lowercase letter."
        return valid

    if password != confirm_password:
        valid = False, "Passwords do not match."
        return valid 

    _saveUSer(user,valid[0])
    
    return True, "Password is valid."

def _saveUSer (user , valid):
    if not valid:
        return False
    else:
        user = {
        "username":user.get("email"),
        "email":user.get("username"),
        "password":user.get("password")
        
        }
        dbnewUser.append(user)
    print (dbnewUser)

@app.route("/bordercross/capture" ,methods=["GET"])
def captureShipment():
    global shipments_data
    global shipment
    
    
    if request.method == "GET":
        embarque = request.args.get('embarque')
        cliente = request.args.get('cliente')
        referencia = request.args.get('referencia')
        operacion = request.args.get('operacion')
        origen = request.args.get('origen')
        destino = request.args.get('destino')
        trailer = request.args.get('trailer')
        sello = request.args.get('sello')
        
    
        if str(operacion) == "1":
            tipoOperacion = "Importacion"
        else:
            tipoOperacion = "Exportacion"
    
        shipment = {
       
        'embarque':embarque,
        'tipoOperacion':tipoOperacion,
        'trailer':trailer,
        'referencia':referencia,
        'sello':sello,
        'cliente':cliente,
        'origen':origen,
        'destino':destino
      
    }
        shipments_data.append(shipment)
        print(shipments_data)
        return render_template("bordercross.html",shipments=shipments_data)
    
    return redirect("displayTacking")


@app.route("/bordercross/update", methods=["post"])
def updateShipment():
    
    # Access form data using request.form with get() and error handling
    unidad = request.form.get('unidad')
    return shipments_data[0]

@app.route('/bordercross')
def displayTacking():
    
    #extrack the data from the Database
    
    return render_template("bordercross.html")
app.run()