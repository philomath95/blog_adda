from blog_app import app, bcrypt, db
from flask import redirect, render_template, url_for, request, flash
from .models import Register

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile')
def Profile():
    return render_template('profile.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        cm_password = request.form.get('confirmed_password')
       
       #checking for existing username and email
        validate_username = Register.query.filter_by(username=username).first()
        validate_email = Register.query.filter_by(email=email).first()


        if validate_username or validate_email:
            print("This Account is Already Exist!")
            return redirect(url_for('LogIn'))
    
        if password!=cm_password:
            print("password is not matching!")
        else:
            hashed_pw = bcrypt.generate_password_hash(password)
            new_user = Register(username=username, email=email, password=hashed_pw, confirm_password=hashed_pw)
            db.session.add(new_user)
            db.session.commit()
            print("Account has been Created Successfully")
            return redirect(url_for('LogIn'))

    return render_template('auth/register.html')
    


@app.route('/login')
def LogIn():
    return render_template('auth/login.html')

