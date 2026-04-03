from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = 'devKey_81347525mverka'

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/sobre-nosotros')
def sobre_nosotros():
    return render_template('sobre-nosotros.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mail = Mail(app)

@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['nombre']
    email = request.form['email']
    mensaje = request.form['mensaje']

    msg = Message(
    subject=f"Nuevo mensaje de {nombre}",
    sender=app.config['MAIL_USERNAME'], 
    recipients=["eduvigisdiaz12@gmail.com"],
    body=f"De: {nombre} <{email}>\n\n{mensaje}"
    )

    try:
        mail.send(msg)
        flash('¡Gracias por contactarnos, te responderemos pronto!')
    except Exception as e:
        flash(f'Ocurrió un error al enviar el correo: {e}')

    return redirect(url_for('contacto'))

if __name__ == '__main__':
    app.run(debug=True)
