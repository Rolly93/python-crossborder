import sqlalchemy
from flask_login import LoginManager,login_user
from flask import Flask, render_template,request,redirect,url_for
from werkzeug.security import check_password_hash ,check_password_hash , generate_password_hash


from model import db, Users
app = Flask(__name__)

@app.route('/newuser', methods=['GET', 'POST'])
def newuser():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        confirm_password = request.form["confirm_password"]
        
        print(request.form)
        if username and password and email and confirm_password:
            if password == confirm_password:
                hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
                try:
                    new_user = Users(
                        username=username,
                        email=email,
                        password=hashed_password
                    )
                    #db.session.add(new_user)
                    #db.session.commit()
                except sqlalchemy.exc.IntegrityError:
                    return redirect(url_for('newuser') + '?error=user-or-email-exist')
                return render_template('login.html')
            else:
                return redirect(url_for('newuser') + '?error=password-mismatch')
        else:
            return redirect(url_for('newuser') + '?error=missing-fields')
    return render_template('newuser.html')
        


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        
        
        username = request.form.get("email")
        password = request.form.get("password")
        print('pass', str(password), 'user', username)
        #user = Users.query.filter_by(username=username).first()
        
        #me falta realizar consulta y verifiacion de identidad
        return render_template('bordercross.html')
    return render_template('login.html')




@app.route('/')
def home():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)