from flask import Flask, jsonify

# Para iniciar, creamos una instancia de la aplicación Flask utilizando la sintaxis app = Flask(__name__)

app = Flask(_name_)

#Posteriormente, generamos una lista de nombres de individuos. Aunque esta lista puede generarse dinámicamente, en este ejemplo la definiremos de manera estática.


personas = ["Mercedes", "Julio", "Mario", "Camilo"]

#A continuación, definimos la ruta del endpoint que utilizaremos para manejar las solicitudes.


@app.route('/personas', methods=['GET'])
def obtener_personas():

#Aquí convertimos la lista de nombres al formato JSON para que sea legible tanto en nuestro navegador como en otras aplicaciones.

    return jsonify(personas)

#Ejecutar la aplicacion Flask

if _name_ == '_main_':
    app.run(debug=True)