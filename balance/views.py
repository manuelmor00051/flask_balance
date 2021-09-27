from . import app
from flask import render_template, request, redirect, url_for
from balance.models import ListaMovimientos, Movimiento, ValidationError

@app.route('/')
def index():
    lm = ListaMovimientos()
    lm.leer()
    return render_template('inicio.html', items= lm.movimientos)

@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'GET':
        return render_template("nuevo_movimiento.html", errores = [], form={"fecha": "", "concepto": "", "cantidad": ""})
    else:
        datos = request.form #request.form trae los datos del formulario
        try:
            movimiento = Movimiento(datos)
        except ValidationError as msg:
            return render_template("nuevo_movimiento.html", errores = [str(msg)], form=datos)
        lm = ListaMovimientos()
        lm.leer()
        lm.anyadir(datos)
        lm.escribir()
        return redirect(url_for("index")) #Redirecciona a la ruta que tiene la funcion "index"