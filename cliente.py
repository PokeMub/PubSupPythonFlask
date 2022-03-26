import json
import os
import time
from flask import Flask, jsonify, request
import requests
from pprint import pprint
url = "http://10.0.1.3:8080"
fila_msgs = []
conf = []

def client():
    opc = None

    while opc != "4" :
        os.system('clear') or None
        print("1 - Logar")
        print("2 - Criar Conta")
        print("4 - Sair")
        opc = input('Digite uma Opcao: ')
        if opc == '1' :
            os.system('clear') or None
            email = input("Digite o email: ")
            senha = input("Digite a senha: ")
            msg= {}
            msg ['codigo'] = 1
            msg ['codigo2'] = 1
            msg ['emaill'] = email
            msg ['senhaa'] = senha   
            msg_json = json.dumps(msg)
            r = requests.get(f"{url}/logar",json=msg_json)
            recebimento = r.json()
            data = recebimento
            data_converted = json.loads(data)
            confirmacao = data_converted['confirmacao']
            conf.append(confirmacao)

        if opc == '2':
            os.system('clear') or None
            nome = input("Digite o seu nome: ")
            dataNascimento = input("Digite sua data Nascimento: ")
            cpf = input("Digite seu cpf: ")
            email = input("Digite seu Email: ")
            senha = input("Digite sua senha: ")
            msg= {}
            msg ['codigo'] = 2
            msg ['codigo2'] = 2
            msg ['nomee'] = nome
            msg ['dataNascimentoo'] = dataNascimento 
            msg ['cpff'] = cpf
            msg ['emaill'] = email
            msg ['senhaa'] = senha 
            msg_json = json.dumps(msg)
            ri = 'sim'
            r = requests.get(f"{url}/cadastrar",json=msg_json)

        opcEntrada = None       
        time.sleep(3)
        os.system('clear') or None
        fant = conf

        if(str(fant) == '[\'sim\']'):
            opcEntrada = 10
            conf.pop(0)

        else:
            opcEntrada = None 

        if opcEntrada == None :
            if(ri == 'sim'):
                print("Cadastro realizado com sucesso")
                ri = 'nao'
            else: 

                print("Houve um erro de conecçao tente mais tarde ou sua senha/login estao invalidos")
            time.sleep(5)

        if opcEntrada == 10 :
            print("Login Realizado com Sucesso")
            opcEntrada = 11
            time.sleep(3)

        if opcEntrada == 11 : 
            while opc != '4':
                os.system('clear') or None
                print(" 1 - Listar Itens")
                print(" 2 - Perfil ")
                print(" 3 - Historico de Compra")
                print(" 4 - Sair")
                opc = input('Digite sua Opçao: ')
                if opc == '1' :
                    os.system('clear') or None
                    print("Lista dos produtos")
                    msg= {}
                    msg ['codigo'] = 7
                    msg_json = json.dumps(msg)
                    #fila_msgs.append(msg_json)
                    r = requests.get(f"{url}/listarProduto",json=msg_json)
                    recebimento = r.json()    
                    data = recebimento
                    data_converted = json.loads(data) 
                    #pr = data_converted['raa']
                    contador = data_converted['contador']
                    li = []
                    i=0
                    vallor = 'val'
                    f = int(contador)
                    for linha in range(f+1):
                        vallor = 'val' + str(i)
                        li.append(data_converted[vallor])
                        i = i +1
                    i=0
                    for linha in range(f+1):
                        print("Codigo: ",i, "  item: " ,li.pop(0))
                        i = i +1

                    time.sleep(10)
                    opc = input("Digite o Codigo do produto: ")
                    os.system('clear') or None
                    print("Dados do cartao")
                    nomeTitular = input("Digite o nome do titular do cartao: ")
                    codigoCartao = input("Digite o codigo do cartao: ")
                    bandeiraCartao = input("Digite a bandeira: ")

                    msg= {}
                    msg ['codigo'] = 9
                    msg ['emaill'] = email
                    msg ['status'] = 'Enviado_Para_Analise'
                    msg ['itencodigo'] = opc
                    msg ['nometitu'] = nomeTitular
                    msg ['codcart'] = codigoCartao
                    msg ['bandeira'] = bandeiraCartao
                    msg_json = json.dumps(msg)
                    #fila_msgs.append(msg_json)
                    r = requests.get(f"{url}/enviarStatus",json=msg_json)
                    opc = None

                if opc == '2' :
                    msg= {}
                    msg ['codigo'] = 4
                    msg ['emaill'] = email
                    msg_json = json.dumps(msg)
                    r = requests.get(f"{url}/perfil",json=msg_json)
                    recebimento = r.json()
                    data = recebimento
                    data_converted = json.loads(data) 
                    nome =  data_converted['nomee']
                    dataNasc = data_converted['dataNascimentoo']
                    cpf = data_converted['cpff']
                    email = data_converted['emaill'] 
                    senha = data_converted['senhaa']
                    os.system('clear') or None
                    print("       lista dos dados do usuario")
                    print("Nome : " + nome)
                    print("Data de Nascimento : " + dataNasc)
                    print("CPF : " + cpf)
                    print("Email : " + email)
                    print("Senha : " + senha)
                    time.sleep(10)

                if opc == '3' :
                    msg= {}
                    msg ['codigo'] = 13
                    msg ['emaill'] = email
                    msg_json = json.dumps(msg)
                    #fila_msgs.append(msg_json)
                    os.system('clear') or None
                    print("Lista de historio de compra")
                    r = requests.get(f"{url}/historico",json=msg_json)
                    recebimento = r.json()    
                    data = recebimento
                    data_converted = json.loads(data) 
                    codigo =  data_converted['codigo']
                    #pr = data_converted['raa']
                    contador = data_converted['contador']
                    li = []
                    i=0
                    vallor = 'val'
                    f = int(contador)
                    for linha in range(f+1):
                        vallor = 'val' + str(i)
                        li.append(data_converted[vallor])
                        i = i +1
                    i=0
                    for linha in range(f+1):
                        print("Codigo: ",i, "  item: " ,li.pop(0))
                        i = i +1
                    
                    time.sleep(10)
            opc=None


if __name__ == "__main__":
    client()