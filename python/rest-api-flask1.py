from flask import Flask, jsonify, abort, make_response, request, render_template
import mysql.connector
import os
app = Flask(__name__)

conn_obj = mysql.connector.connect(host="localhost",user="root",password = '12345', database="Catalogo")
print(conn_obj)
con_obj= conn_obj.cursor()
print(con_obj)

#query= "SELECT * FROM Componente"
#con_obj.execute(query)
#result= con_obj.fetchall()
#final_result=[list(i) for i in result]
#print(final_result[0])

#@app.route('/<string:page_name>/')
#def render_static(page_name):
#    return render_template('%s.html' % page_name)

@app.route('/html/listadoC')
def render_components():
    query= "SELECT * FROM Componente"
    con_obj.execute(query)
    result= con_obj.fetchall()
    return render_template('ListadoComponentes.html', final_result=result)

@app.route('/html/listadoC/<id>')
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
    

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 4444)))