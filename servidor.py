#from re import T
#from contextlib import ContextDecorator
import socket
import _thread
import json
from time import time
#from psutil import cpu_count
import zmq
import sys
import time
from flask import Flask, jsonify, request
from libcloud import requests
import pprint
app = Flask(__name__)
IP_ADDRESS = '10.0.1.1'
TOPIC = None
fila_msgs = []
fil = []

@app.route("/enviarStatus", methods=["GET", "POST"])
def enviarStatus():

    if request.method == "GET":
        msg_json = request.json
        pprint.pprint(msg_json)
        msg_json = str(msg_json)
        arquivo = open('statu.txt', 'a')
        arquivo.write(msg_json)
        arquivo.write("\n")
        arquivo.close()
        #msg_json = json.dumps(msg_json)
        fila_msgs.append(msg_json) 

        return (
            jsonify({"id": 'opa'})
        )
    else:
        return "", 404
        

@app.route("/listarProduto", methods=["GET", "POST"])
def listarProduto():
    if request.method == "GET":
        msg_json = request.json
        pprint.pprint(msg_json)
        msg_json = str(msg_json)
        data = msg_json
        data_converted = json.loads(data)
        arquivo = open('itens.txt', 'r')
        i=0
        tes = 'codigo'
        msg= {}
        msg [tes] = 8
        vallor = 'val'
        for linha in arquivo:

            val = linha.split()
            print(val[0],val[1])
            vallor = 'val' + str(i)
            msg [vallor] = val[0] + val[1]
            i = i +1
        msg ['contador'] = i -1
        msg_json = json.dumps(msg)
        #fila_msgs.append(msg_json) 
        arquivo.close()
        return (
            jsonify(msg_json)
        )
    else:
        return "", 404

@app.route("/historico", methods=["GET", "POST"])  
def historico():
    if request.method == "GET":
        msg_json = request.json
        pprint.pprint(msg_json)
        msg_json = str(msg_json)
        data = msg_json
        data_converted = json.loads(data)
        emaill = data_converted['emaill']
        emaill = '"' + emaill + '"' + ','
        arquivo = open('statu.txt', 'r')
        i=0
        tes = 'codigo'
        msg= {}
        msg [tes] = 15
        vallor = 'val'
        for linha in arquivo:
            val = linha.split()
            #print(val[0],val[13])
            if(emaill == val[3]):
                #print("teste")
                vallor = 'val' + str(i)
                msg [vallor] = val[0] + val[1]+  val[2]+   val[3]+  val[4]+  val[5]+  val[6]+  val[7]+  val[8]+  val[9]+  val[10]+  val[11]+  val[12]+ val[13] 
                i = i +1
        msg ['contador'] = i -1
        msg_json = json.dumps(msg)
        #fila_msgs.append(msg_json) 
        arquivo.close()
        print(msg_json)
        return (
            jsonify(msg_json)
        )
    else:
        return "", 404

@app.route("/perfil", methods=["GET", "POST"])  
def verPerfil():
    if request.method == "GET":
        msg_json = request.json
        pprint.pprint(msg_json)
        msg_json = str(msg_json)
        data = msg_json
        data_converted = json.loads(data)
        email = data_converted['emaill']
        arquivo = open('cadastro.txt', 'r')
        email = '"' + email + '"' + ','        
        for linha in arquivo:
            val = linha.split()
            #print(val[11])
            if (email == val[11] ):
                print(val[11])
                msg= {}
                msg ['codigo'] = 6
                msg ['nomee'] = val[5]
                msg ['dataNascimentoo'] = val[7]
                msg ['cpff'] = val[9]
                msg ['emaill'] = val[11]
                msg ['senhaa'] = val[13]
                msg_json = json.dumps(msg)
                fil.append(msg_json) 
        return (
            jsonify(fil.pop(0))
        )
    else:
        return "", 404

@app.route("/cadastrar", methods=["GET", "POST"])    
def serv():

    if request.method == "GET":
        msg_json = request.json
        pprint.pprint(msg_json)
        msg_json = str(msg_json)
        arquivo = open('cadastro.txt', 'a')
        arquivo.write(msg_json)
        arquivo.write("\n")
        arquivo.close()
        return (
            jsonify({"id": 'opa'})
        )
    else:
        return "", 404

@app.route("/logar", methods=["GET", "POST"])
def logar():
    if request.method == "GET":
        msg_json = request.json
        pprint.pprint(msg_json)
        msg_json = str(msg_json)
        data = msg_json
        data_converted = json.loads(data)
        codigo = data_converted['codigo']
        codigo2 = data_converted['codigo2']
        email = data_converted['emaill']
        senha = data_converted['senhaa']
        arquivo = open('cadastro.txt', 'r')
        email = '"' + email + '"' + ','
        senha = '"' + senha + '"' + '}'
        print(senha)
        print(email)
        for linha in arquivo:
            val = linha.split()
            if (email == val[11]) & (senha == val[13]):
                print(val[11],val[13])
                msg= {}
                msg ['codigo'] = 3
                msg ['codigo2'] = 1
                msg ['confirmacao'] = 'sim'
                msg_json = json.dumps(msg)
                fil.append(msg_json) 
                cont = 2;
        if cont == 1:
            msg= {}
            msg ['codigo'] = 3
            msg ['codigo2'] = 1
            msg ['confirmacao'] = 'nao'
            msg_json = json.dumps(msg)
            fil.append(msg_json) 
        arquivo.close()
        return (
            jsonify(fil.pop(0))
        )
    else:
        return "", 404
        
   
 
def enviar():
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUB)
    sock.connect(f"tcp://{IP_ADDRESS}:5500")
    codigo = 5
    while True:
        if(len(fila_msgs) == 0):
            pass
        else:
            data = fila_msgs.pop(0)
            data_converted = json.loads(data)
            codigo = data_converted['codigo']
        if(codigo == 9):
            msg_json = data
            TOPIC = 'enviarcontrrr'   
            sock.send_string(f"{TOPIC}", flags=zmq.SNDMORE)
            sock.send_json(msg_json) 
            codigo = 5 
 

def receberConfirmCart():
    while True:
        ctx = zmq.Context()
        sock = ctx.socket(zmq.SUB)
        sock.connect(f"tcp://{IP_ADDRESS}:5501")   
        TOPIC = 'confirmadasooo'
        sock.subscribe(f"{TOPIC}")
        msg_string = sock.recv_string()
        msg_json = sock.recv_json()
        print(msg_json)
        arquivo = open('statu.txt', 'a')
        arquivo.write(msg_json)
        arquivo.write("\n")
        arquivo.close() 

 
def server():
    _thread.start_new_thread(enviar,())
    _thread.start_new_thread(receberConfirmCart,())

    app.run(host="0.0.0.0", port=8080)
    while True:
        pass

if __name__ == "__main__":
    server()


