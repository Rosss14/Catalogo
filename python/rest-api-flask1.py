from flask import Flask, jsonify, abort, make_response, request, render_template, url_for, redirect
import mysql.connector
import os
app = Flask(__name__)

conn_obj = mysql.connector.connect(host="localhost",user="root", password = '12345', database="Catalogo")

con_obj= conn_obj.cursor()

#@app.route('/<string:page_name>/')
#def render_static(page_name):
#    return render_template('%s.html' % page_name)

@app.route('/listadoC')
def render_components():
    query= "SELECT * FROM Componente"
    con_obj.execute(query)
    result= con_obj.fetchall()
    return render_template('ListadoComponentes.html', final_result=result)

@app.route('/listadoC/<id>')
def render_component(id):
    #id=int(id)
    query= "SELECT * FROM Componente WHERE component_id = " + id
    con_obj.execute(query)
    result= con_obj.fetchone()
    print(result)
    #component =[component for component in result if component[0]==id]
    if len(result)==0:
        abort(404)
    return render_template('Componente.html', final_result=result)

@app.route('/')
def render_medicines():
    query= "SELECT * FROM medicamento"
    con_obj.execute(query)
    result= con_obj.fetchall()
    return render_template('ListadoMedicamentos.html', final_result=result)

@app.route('/listadoM/<id>')
def render_medicine(id):
    query= "SELECT * FROM medicamento WHERE medicamento_id = " + id
    con_obj.execute(query)
    result= con_obj.fetchone()
    print(result)
    if len(result)==0:
        abort(404)
    return render_template('Medicamento.html', final_result=result)

@app.route('/listadoM/create', methods = ('GET', 'POST'))
def createMedicine():

    if request.method == 'POST':
        nombre = request.form['nombre']
        grupo = request.form['grupo']
        dosis = request.form['dosis']
        efectos_secundarios = request.form['efectos']
        laboratorio = request.form['lab']
        profesional = request.form['prof']

        if not nombre:
            #flash('Title is required!')
            print('Name required')
        else:
            con_obj.execute('INSERT INTO medicamento (nombre, grupoTerapeutico, dosisDiaria, efectosSecundarios, laboratorio, profesional) VALUES (%s, %s, %s, %s, %s, %s)',
                         (nombre, grupo, dosis, efectos_secundarios, laboratorio, profesional))
            conn_obj.commit()
            return redirect(url_for('render_medicines'))

    return render_template('createMedicine.html')

@app.route('/listadoM/<id>/edit', methods = ('GET', 'POST'))
def editMedicine(id):

    query= "SELECT * FROM medicamento WHERE medicamento_id = " + id
    con_obj.execute(query)
    medicamento = con_obj.fetchone()

    if request.method == 'POST':
        nombre = request.form['nombre']
        grupo = request.form['grupo']
        dosis = request.form['dosis']
        efectos_secundarios = request.form['efectos']
        laboratorio = request.form['lab']
        profesional = request.form['prof']

        if not nombre:
            #flash('Title is required!')
            print('Name required')
        else:
            con_obj.execute('UPDATE medicamento SET nombre=%s, grupoTerapeutico=%s, dosisDiaria=%s, efectosSecundarios=%s, laboratorio=%s, profesional=%s'
                         ' WHERE medicamento_id = %s',
                         (nombre, grupo, dosis, efectos_secundarios, laboratorio, profesional, id))
            conn_obj.commit()
            return redirect(url_for('render_medicines'))

    return render_template('editMedicine.html', drug = medicamento)

@app.route('/listadoM/<int:id>/delete', methods=('POST',))
def delete_medicine(id):
    con_obj.execute("SELECT * FROM medicamento WHERE medicamento_id = " + str(id))
    medicamento = con_obj.fetchone()
    con_obj.execute('DELETE FROM medicamento WHERE medicamento_id = %s', (id,))
    conn_obj.commit()
    return redirect(url_for('render_medicines'))

#if __name__ == "__main__":
#    app.run(host=os.getenv('IP', '0.0.0.0'),
#            port=int(os.getenv('PORT', 4444)))

if __name__ == "__main__":
    app.run()
