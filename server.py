from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key="secret"

@app.route('/')
def index():
    if 'count' not in session:
        session['count']=0
    else:
        session['count']+=1
        
    if 'key_name' in session:
        print('la llave existe!')
    else:
        print("la llave 'key_name' NO existe")
    return render_template("index.html")

@app.route('/reseteo')
def reseteo():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)  


"""
    if 'key_name' in session:
    print('la llave existe!')
else:
    print("la llave 'key_name' NO existe")

session.clear()		# borra todas las claves
session.pop('key_name')		# borra una clave específica
"""