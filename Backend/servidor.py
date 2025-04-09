from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)

mongo_uri = "mongodb+srv://nxvxv:Quince15@cluster0.psv8nqy.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)

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

if __name__ == '__main__':
    app.run(debug=True)