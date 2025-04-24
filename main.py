from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
import db
from models import Tarea
from datetime import datetime


app=Flask(__name__)
@app.route("/")#añadimos un decorador para que se puede visualizar en la web, añadimos endpoint
#el / se refiere a la raiz
def home():
    todas_las_tareas = db.session.query(Tarea).all()
    for i in todas_las_tareas:
        print(i)
    #en este return podemos enviar todas las variables que queramos
    return render_template("index.html", lista_de_tareas=todas_las_tareas)


#usamos el metodo post para decir que esa ruta es responsable del envio de info. en este caso la información del form
@app.route("/crear-tarea",methods=["POST"])
def crear():
    #usamos request.form para acceder a lo que me devuelve un formulario
    #hacemos un slicing ya que el form nos devuelve un diccionario
    fecha_str = request.form['fecha_limite']
    fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d').date()

    tarea=Tarea(contenido=request.form['contenido_tarea'], hecha=False,fecha=fecha_obj)
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for('home'))


#ruta para eliminar las tareas
@app.route("/eliminar-tarea/<id>")
def eliminar(id):
    tarea=db.session.query(Tarea).filter(Tarea.id==int(id)).delete()
    db.session.commit()
    return redirect(url_for('home'))
#ruta para camnbiar el estado de la tarea (True o False)
@app.route("/tarea-hecha/<id>")
def hecha(id):
    tarea=db.session.query(Tarea).filter(Tarea.id==int(id)).first()
    tarea.hecha=not(tarea.hecha)
    db.session.commit()
    return redirect(url_for('home'))
if __name__=="__main__":
    #creamos la base de datos
    db.Base.metadata.create_all(bind=db.engine)
    app.run(debug=True)