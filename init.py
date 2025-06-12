from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS 


app = Flask(__name__)
# Configuración de la base de datos existente
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(app.instance_path, 'noticias.db') # Cambia si usas otra
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# cors = CORS(app, resources={
#     r"/api/*": {
#         "origins": ["http://localhost:3000"],
#         "methods": ["GET", "POST", "OPTIONS"],
#         "allow_headers": ["Authorization", "Content-Type"]
#     }
# })


# Inicializar extensiones
db = SQLAlchemy(app)
api = Api(app)
