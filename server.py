import os
from flask import Flask, render_template , request , redirect , url_for , flash
from werkzeug import secure_filename
from class_ugc import ugc
from class_categorias import categoria
from class_area import area
from class_profesional import profesional

app = Flask(__name__)
app.secret_key = "frjkfjierjklsjk5343"
# Carpeta de subida
app.config['UPLOAD_FOLDER'] = './static/fotos'


@app.route('/')
def index():
    lugc = ugc()
    listado_ugcs = lugc.listado_ugcs()

    l_categoria = categoria()
    listado_categorias = l_categoria.listado_categorias()

    l_area = area()
    listado_areas = l_area.listado_areas()
    return render_template('index.html', listado_ugc = listado_ugcs, listado_categorias = listado_categorias,\
         listado_areas = listado_areas)


@app.route('/nuevo_prof', methods=['POST'])
def nuevo():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        f = request.files['foto']
        filename = secure_filename(f.filename)
        if len(filename)>0 :
            # Guardamos el archivo en el directorio "imagenes"
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else :
            filename =""

        nuevo_profesional = profesional(0, request.form['identificacion'], request.form['apellido1'],\
             request.form['apellido2'], request.form['nombre'], request.form['categoria'],\
                  request.form['ugc'], request.form['area'], filename)
        nuevo_profesional.nuevo_profesional()
      

        flash('Profesional Creado')
    return redirect(url_for('index'))


@app.route('/buscar_prof')
def buscar_profesionales():
    return render_template('buscar_prof.html')


@app.route('/listado_profesionales', methods=['POST'])
def listado_profesionales():
    if request.method == 'POST':
        prof = profesional(0,0,0,0,0,0,0,0,0)
        dni = request.form['dni']  
        ap1 = request.form['ap1']
        ap2 = request.form['ap2'] 
        if len(dni)>1:
            #buscar por dni
            lista_busqueda = prof.busca_dni(dni)
        else:
            #buscar por apellido/s
            lista_busqueda = prof.busca_apellidos(ap1, ap2)
        del prof
        return render_template('buscar_prof.html', dni=dni, ap1 = ap1, ap2=ap2, lista_busqueda=lista_busqueda)


@app.route('/delete_prof', methods = ['GET'])
def delete_prof():
    codigo = request.args.get('valor')
    prof = profesional(codigo,0,0,0,0,0,0,0,0)
    prof.elimina_profesional()
    del prof


@app.route('/select_profesional/<id>')
def selecionar_prof(id):
    lugc = ugc()
    listado_ugcs = lugc.listado_ugcs()
    l_categoria = categoria()
    listado_categorias = l_categoria.listado_categorias()
    l_area = area()
    listado_areas = l_area.listado_areas()
    del lugc
    del l_categoria
    del l_area

    prof = profesional(id,0,0,0,0,0,0,0,0) 
    datos_prof = prof.seleccionar_profesional()
    del prof
    return render_template('modifica_prof.html',prof = datos_prof[0] ,listado_ugc = listado_ugcs,\
         listado_categorias = listado_categorias, listado_areas = listado_areas)


@app.route('/update_prof/<id>', methods = ['POST'])
def modifica_profesional(id):
    lugc = ugc()
    listado_ugcs = lugc.listado_ugcs()
    l_categoria = categoria()
    listado_categorias = l_categoria.listado_categorias()
    l_area = area()
    listado_areas = l_area.listado_areas()
    del lugc
    del l_categoria
    del l_area

    if request.method == 'POST':
        f = request.files['foto']
        filename = secure_filename(f.filename)
        # Guardamos el archivo en el directorio "imagenes"
        if len(filename)>0:
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else :
            filename = ""
        prof_modificado = profesional(id, request.form['ident'], request.form['ap1'], request.form['ap2'],\
             request.form['nombre'],request.form['categoria'],request.form['ugc'],request.form['area'],filename)
       
        prof_modificado.modifica_profesional()
        del prof_modificado
        flash("Profesional Modificado.")
        muestra_prof = profesional(id,0,0,0,0,0,0,0,0)
        datos_profesional = muestra_prof.seleccionar_profesional()
        del muestra_prof
        return render_template('modifica_prof.html',prof = datos_profesional[0] ,listado_ugc = listado_ugcs,\
             listado_categorias = listado_categorias, listado_areas = listado_areas)



if __name__=="__main__":
    app.run(port=8000,debug = True)