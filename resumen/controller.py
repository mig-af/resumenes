from flask_restful import Resource, reqparse
from .repository import ResumenRepository
import json
from .model import Resumen

repository = ResumenRepository()
parser = reqparse.RequestParser()
parser.add_argument('status', required=True, help='El campo status es obligatorio', type=bool)
parser.add_argument('data', required=True, help='El campo data es obligatorio', type=dict)



class ResumenController(Resource):


    def get(self, date=None):
        
        if(date != None):
            resp = repository.find_by_date(date=date)
            
            if(resp):
                print(type(resp))
                return [{"id":i.id, "resumen":i.cuerpo, "url":i.url} for i in resp], 200
            else:
                return {"Data":"No hay datos"}, 404



        print("get iniciado")
        data = repository.get_all()

        if(data):
            return [{"id":i.id, "resumen":i.cuerpo, "url":i.url} for i in data], 200
        else:
            return {"Data":"No hay datos"}, 404
        

    def post(self):
        data = parser.parse_args()
        
        print(type(data))
        ia_resumen = data
        try:
            
            print(type(ia_resumen["status"]))
            resumenes = []
            if(ia_resumen["status"] == True):
                for i in ia_resumen["data"]["resumen"]:
                    datos = {"cuerpo":i[0], "url":i[1][0]}
                    resumenes.append(Resumen(datos))

                for resumen in resumenes:
                    print(type(resumen))
                    print(resumen.url)
                    repository.save(resumen)
                #print(data)
                return data, 201
            else:
                return data, 400
        except Exception as e:
       
            return data, 400




    