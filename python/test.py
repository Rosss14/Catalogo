from flask import Flask, jsonify, abort, make_response, request, render_template, url_for, redirect
import mysql.connector
import os


conn_obj = mysql.connector.connect(host="localhost",user="root", password = '12345', database="Catalogo")

con_obj= conn_obj.cursor()

query= "SELECT * FROM medicamento WHERE medicamento_id = " + str(3)

con_obj.execute(query)

medicamento = con_obj.fetchone()

print(medicamento)
