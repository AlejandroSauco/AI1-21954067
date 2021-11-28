#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().system('pip install pyrebase4')


# In[10]:


import threading
import sys
import socket
import pickle
import os


# In[20]:


import pyrebase as py


# In[2]:


firebaseConfig = {
  "apiKey": "AIzaSyAfMJEIxKfVX_eKTrIoVdXg09QY9USMlzc",
  "authDomain": "functions-real-case-pbi.firebaseapp.com",
  "databaseURL": "https://functions-real-case-pbi-default-rtdb.firebaseio.com",
  "projectId": "functions-real-case-pbi",
  "storageBucket": "functions-real-case-pbi.appspot.com",
  "messagingSenderId": "212033978800",
  "appId": "1:212033978800:web:e1d63004db5d6c6fe89675",
  "measurementId": "G-N23MB60FQV"
}


# In[8]:


firebaseConfigSauco = {
  apiKey: "AIzaSyDjoPGps40aiM0aZFVsWK-6GjETQnQ-DJ4",
  authDomain: "practica25-11-2021-7c831.firebaseapp.com",
  databaseURL: "https://practica25-11-2021-7c831-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "practica25-11-2021-7c831",
  storageBucket: "practica25-11-2021-7c831.appspot.com",
  messagingSenderId: "851304814282",
  appId: "1:851304814282:web:aa198ca483fd599d910633",
  measurementId: "G-QN24YSLVNW"
}


# In[3]:


firebase = py.initialize_app(firebaseConfig)


# In[9]:


firebase = py.initialize_app(firebaseConfigSauco)


# In[10]:


sing_up_in=firebase.auth()


# In[12]:


mail=input("Dame mail")


# In[13]:


passw = input("Dame contrasena")


# In[14]:


print(f'Su mail es: {mail} y su contrasena es: {passw}')


# In[15]:


user=sing_up_in.create_user_with_email_and_password(mail,passw)


# In[16]:


sing_up_in.send_email_verification(user['idToken'])


# In[17]:


user


# In[18]:


ddbb=firebase.database()


# In[19]:


ddbb.child('pcd/credenciales/21954067').set(user)


# In[21]:


ddbb.child('pcd/credenciales/21954067/token').set(firebaseConfigCrishina)


# In[22]:


ddbb.child('pcd/credenciales/21954067/user').set(firebaseConfigCrishina)


# In[23]:


storage = firebase.storage()


# In[25]:


storage.child('classparticipation/21954067/21954067.png').put('PruebaPCD.png')


# # Empieza el Cliente

# In[ ]:


class Cliente():
    host_ = input("Introduce tu direccion ip: ")
    port_ = int(input("Introduce tu puerto: "))
    nick = input("Nombre de usuario: ")

    nicks = []

    def __init__(self,host=socket.gethostname(), port=port_, nickname=nick):
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
                try:
                    with open("u21954067.txt", "a+") as Hist:
                        Hist.write(nickname + ": " + msg + "\n")
                except Exception as e:
                    print("Aca hubo un error")
                    print(e)
                if msg != 'Q':
                    self.enviar(nickname + ": " + msg)#funcion para enviar --> nombre: (mensaje)
                else:
                    print(" **** TALOGOOO  ****")
                    self.sock.close()
                    sys.exit()
        except:
            raise Exception


# In[16]:


def recibir(self):
       while True:
           try:
               data = self.sock.recv(32)
               if data:
                   print(pickle.loads(data))
           except:
               pass


# In[17]:


def enviar(self, msg):
       self.sock.send(pickle.dumps(msg))#envia el mensaje al servidor 


# In[18]:


def enviarNick(self, nick_):
       self.sock.send(pickle.dumps(nick_))#envia los nicks al servidor


# In[19]:


c = Cliente()


# In[ ]:




