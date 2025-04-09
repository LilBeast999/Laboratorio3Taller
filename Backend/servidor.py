from flask import Flask, request, jsonify  # <-- Se agregó jsonify
from pymongo import MongoClient
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

mongo_uri = "mongodb+srv://nxvxv:Quince15@cluster0.psv8nqy.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)

# Accede a la base de datos "LaPampara"
db = client["LaPampara"]

# Accede a la colección "fechitas"
fechitas_collection = db["fechitas"]

@app.route('/')
def hello():
    return "¡Hola, Flask!"

@app.route('/testdb')
def test_db():
    try:
        client.admin.command('ismaster')
        return "Conexión exitosa a Mongo Atlas"
    except Exception as e:
        return f"Error al conectar a Mongo Atlas: {e}"

@app.route('/insert')
def insert_data():
    try:
        document = {"fecha": "2025-04-09", "detalle": "Ejemplo de inserción"}
        result = fechitas_collection.insert_one(document)
        return f"Documento insertado con id: {result.inserted_id}"
    except Exception as e:
        return f"Error al insertar documento: {e}"

@app.route('/insert_record', methods=['POST'])
def insert_record():
    try:
        # Se espera que los datos se envíen mediante form-data o x-www-form-urlencoded
        nombre = request.form.get('nombre')
        matricula = request.form.get('matricula')
        hora = request.form.get('hora')
        fecha_str = request.form.get('fecha')

        if not all([nombre, matricula, hora, fecha_str]):
            return "Faltan parámetros", 400

        try:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
        except ValueError:
            return "El formato de fecha debe ser YYYY-MM-DD", 400

        document = {
            "nombre": nombre,
            "matricula": matricula,
            "hora": hora,
            "fecha": fecha  # Se guarda como objeto datetime en MongoDB
        }
        result = fechitas_collection.insert_one(document)
        return f"Documento insertado con id: {result.inserted_id}"
    except Exception as e:
        return f"Error al insertar documento: {e}", 500

@app.route('/get_records', methods=['GET'])
def get_records():
    try:
        documentos = list(fechitas_collection.find())
        resultados = []
        for doc in documentos:
   
            doc['_id'] = str(doc['_id'])

            if 'fecha' in doc and isinstance(doc['fecha'], datetime):
                doc['fecha'] = doc['fecha'].strftime('%Y-%m-%d')
            resultados.append(doc)
        return jsonify(resultados)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)