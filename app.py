from init import app, api
from resumen.controller import ResumenController   


# Enlace de ruta al recurso

api.add_resource(ResumenController, "/api", "/api/<int:date>")


if __name__ == '__main__':
    
    app.run(host='0.0.0.0',port= 4000, debug=True)
