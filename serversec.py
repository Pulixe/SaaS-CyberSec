import os
import pyotp
import smtplib
# using flask_restful para servir el codigo de verificacion
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import reqparse,abort,Resource, Api
  
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app) 
CORS(app)
#se genera la llave base para generar los 6 digitos    
key = pyotp.random_base32()
totp = pyotp.TOTP(key,6,None,None,None, 60)
seccode = ''
# POST 1: clase que genera y envia el codigo por correo electronico
class getCode(Resource):
    def post(self):
        seccode=totp.now()
        print("el codigo generado es: "+seccode)
        json_data = request.get_json(force=True)
        email = json_data['email']
        print(email)
        FROM = 'jeremi.chacon@utp.ac.pa'
        TO = [email] # must be a list
        SUBJECT = "Codigo de validacion"
        
        TEXT = seccode
        #se arma el mensaje del correo electronico
        message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
        
        # Se envia el correo electronico con el codigo
        server = smtplib.SMTP('smtp.freesmtpservers.com:25')
        server.sendmail(FROM, TO, message)
        server.quit()
        return jsonify({'codigo': seccode})


#POST 2 : Clase que recibe el codigo enviado por el usuario y lo valida
class verifyCode(Resource):
    def post(self):
        #print("el codigo a verificar es: " + totp.now())
        #CODIGO PARA REVISAR EL CODIGO de 6 digitos
        json_data = request.get_json(force=True)
        codigo = json_data['codigo']
        
        if totp.verify(codigo):
            return jsonify({'mensaje':"valido"})
        else:
            return jsonify({'mensaje':"invalido"})
# adding the defined resources along with their corresponding urls
api.add_resource(getCode, '/getcode')
api.add_resource(verifyCode, '/verifyCode')
  
  
# driver function
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug = True, host='0.0.0.0', port=port)