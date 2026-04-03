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

    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <title>Nuevo mensaje</title>
    <style>
    /* Aquí va todo tu CSS */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Open+Sans&display=swap');
    body {{
        font-family: 'Montserrat', 'Open Sans', sans-serif;
        background-color: #ffffff;
        color: #222222;
        line-height: 1.6;
        padding: 20px;
    }}
    h2 {{
        color: #9485df;
        text-align: center;
    }}
    .contenido {{
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        border: 1px solid #eaeaea;
    }}
    p {{
        font-size: 1rem;
        color: #444444;
    }}
    .highlight {{
        font-weight: 700;
        color: #222222;
    }}
    </style>
    </head>
    <body>
        <h2>Nuevo mensaje de contacto</h2>
        <div class="contenido">
            <p><span class="highlight">Nombre:</span> {nombre}</p>
            <p><span class="highlight">Correo:</span> {email}</p>
            <p><span class="highlight">Mensaje:</span><br>{mensaje}</p>
        </div>
    </body>
    </html>
    """

    msg = Message(
    subject=f"Nuevo mensaje de {nombre}",
    sender=app.config['MAIL_USERNAME'], 
    recipients=["eduvigisdiaz12@gmail.com"],
    html=html_content
    )

    try:
        mail.send(msg)
        flash('¡Gracias por contactarnos, te responderemos pronto!')
    except Exception as e:
        flash(f'Ocurrió un error al enviar el correo: {e}')

    return redirect(url_for('contacto'))

if __name__ == '__main__':
    app.run(debug=True)
