from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS 


app = Flask(__name__)
# Configuración de la base de datos existente
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(app.instance_path, 'noticias.db') # Cambia si usas otra
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


DOMAIN = os.environ.get("DOMAIN")

CORS(app, resources={
    # r"/api/*": {
    #     "origins": DOMAIN,
    #     "methods": ["POST"],
    #     "allow_headers": ["Authorization", "Content-Type"]
    # },
    r"/api/*":{
        "origins":"*",
        "methods":["GET", "POST"],

    }
})


# Inicializar extensiones
db = SQLAlchemy(app)
api = Api(app)
