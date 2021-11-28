import threading
import sys
import socket
import pickle
import os
import pyrebase as py

host_ = input("Introduce tu direccion ip: ")
port_ = int(input("Introduce tu puerto: "))
mail = input("Dame mail:")
passw = input("Dame contrasena:")

        firebaseConfig = {
          "apiKey": "AIzaSyDjoPGps40aiM0aZFVsWK-6GjETQnQ-DJ4",
          "authDomain": "practica25-11-2021-7c831.firebaseapp.com",
          "databaseURL": "https://practica25-11-2021-7c831-default-rtdb.europe-west1.firebasedatabase.app",
          "projectId": "practica25-11-2021-7c831",
          "storageBucket": "practica25-11-2021-7c831.appspot.com",
          "messagingSenderId": "851304814282",
          "appId": "1:851304814282:web:aa198ca483fd599d910633",
         " measurementId": "G-QN24YSLVNW"
        }
        
        firebase = py.initialize_app(firebaseConfig)
         sing_up_in=firebase.auth()
        user=sing_up_in.create_user_with_email_and_password(mail,passw)
        
        ddbb=firebase.database()
        ddbb.child('pcd/credenciales/21954067').set(user)
             

class Cliente():

    nicks = []

    def __init__(self,host=socket.gethostname(), port=port_, nickname=mail):
        self.sock = socket.socket()
        self.sock.connect((str(host), int(port)))
        self.nickname = nickname
        try:
            hilo_recv_mensaje = threading.Thread(target=self.recibir)
            hilo_recv_mensaje.daemon = True
            hilo_recv_mensaje.start()
            print('Hilo con PID', os.getpid())
            print('Hilos activos', threading.active_count())
            self.enviarNick(nickname) #envia el nickname al conectarse por primera vez

            while True:
                msg = input('\nEscriba texto ? ** Enviar = ENTER ** Abandonar Chat = Q \n')
                bbdd=firebase.database()
                bbdd.child.("repasoParcial/21535220/215352200").push(msg)
                try:
                    with open("u21954067.txt", "a+") as Hist:
                        Hist.write(nickname + ": " + msg + "\n")
                except Exception as e:
                    print("Aca hubo un error")
                    print(e)
                if msg != 'Q':
                    self.(nickname + ": " + msg)#funcion para enviar --> nombre: (mensaje)
                else:
                    print(" **** TALOGOOO  ****")
                    self.sock.close()
                    sys.exit()
        except:
            raise Exception
    

    def recibir(self):
        while True:
            try:
                data = self.sock.recv(32)
                if data:
                    print(pickle.loads(data))
            except:
                pass

    def enviar(self, msg):
        self.sock.send(pickle.dumps(msg))#envia el mensaje al servidor 

    def enviarNick(self, nick_):
        self.sock.send(pickle.dumps(nick_))#envia los nicks al servidor

     

c = Cliente()
