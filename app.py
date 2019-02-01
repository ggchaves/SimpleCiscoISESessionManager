# coding=utf-8
from flask import Flask, render_template, request, session, jsonify, make_response, redirect as r
from flask_httpauth import HTTPBasicAuth
from flask_bcrypt import Bcrypt
from simplepam import authenticate

import config as c
app = Flask(__name__)
app.secret_key = c.secret_key

bcrypt = Bcrypt(app)
auth = HTTPBasicAuth()

sampleMessagesList=[{'timestamp': " ", 'state': " ", 'userName': " ", 'ipAddresses': " ", 'macAddress': " "}]


@auth.verify_password
def verify_pw(username, password):
    return authenticate(str(username), str(password))

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.route('/')
@auth.login_required
def main():
#    sampleMessageData={'timestamp': "2019-01-24T09:53:18-06:00", 'state': "DISCONNECTED", 'userName': "admin-pc", 'ipAddresses': "172.16.13.25", 'macAddress': "c4:b3:01:b7:42:d1"}
    return render_template('main.html',result=sampleMessagesList)



@app.route('/DoSomething', methods=['POST'])
def predictvalues():

    print(request.form)
    updatedMessagesList=[{'timestamp': "2019-01-24T09:53:18-06:00", 'state': "DISCONNECTED", 'userName': "user-pc", 'ipAddresses': "172.16.13.25", 'macAddress': "c4:b3:01:b7:42:d1"}, {'timestamp': "2019-01-24T09:53:18-06:00", 'state': "DISCONNECTED", 'userName': "user-pc", 'ipAddresses': "172.16.13.25", 'macAddress': "c4:b3:01:b7:42:d2"}, {'timestamp': "2019-01-24T09:53:18-06:00", 'state': "DISCONNECTED", 'userName': "user-pc", 'ipAddresses': "172.16.13.25", 'macAddress': "c4:b3:01:b7:42:d3"}]

    #testing with values sent from the HTML template
    primaryIPinput=request.form['primaryIPinput']
    pxGridServerCAinput=request.form['pxGridServerCAinput']
    pxGridServerCAKeyinput=request.form['pxGridServerCAKeyinput']
    deviceCertinput=request.form['deviceCertinput']
    clientNodeNameinput=request.form['clientNodeNameinput']

    print("primaryIPinput: ",primaryIPinput)
    print("pxGridServerCAinput: ",pxGridServerCAinput)
    print("pxGridServerCAKeyinput: ",pxGridServerCAKeyinput)
    print("deviceCertinput: ",deviceCertinput)
    print("clientNodeNameinput: ",clientNodeNameinput)

    value2="just some more test data"

    #sessions_text="Timestamp: "+sampleMessageData['timestamp']+" State:"+sampleMessageData['state']+" UserName:"+sampleMessageData['userName']+" IP Addresses:"+sampleMessageData['ipAddresses'][0]+" Mac Address:"+sampleMessageData['macAddress']



    #Then return it to HTML

#    return jsonify({'status': 'OK', 'value2': value2});
    return render_template('main.html',result=updatedMessagesList)


if __name__ == "__main__":
	#app.run(threaded=True)
	app.run(host='0.0.0.0', port=5000)