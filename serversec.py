import time
import pyotp
import smtplib
# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import reqparse,abort,Resource, Api
  
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)  
# clase que genera y envia el codigo por correo electronico
class getCode(Resource):
  
    def post(self):
        json_data = request.get_json(force=True)
        email = json_data['email']
        print(email)
        FROM = 'jeremi.chacon@utp.ac.pa'

        TO = [email] # must be a list

        SUBJECT = "Codigo de validacion"

       
        key = pyotp.random_base32()
        totp = pyotp.TOTP(key)
        seccode=totp.now()
        TEXT = seccode
        message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
        
                   # Send the mail
        server = smtplib.SMTP('smtp.freesmtpservers.com:25')
        server.sendmail(FROM, TO, message)
        server.quit()
        return jsonify({'codigo': seccode})
  
  
# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(getCode, '/getcode')
  
  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)