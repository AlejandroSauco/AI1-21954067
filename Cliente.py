import threading
import sys 
import socket
import pickle
import os


class Cliente():
    def mostrarIP():
        ipp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Obtener la información del socket de este programa en este dispositivo
        ipp.connect(("8.8.8.8", 80))
        print("La IP de este dispositivo es:", ipp.getsockname()[0], "\n")
        ipp.close()

    mostrarIP()
    
    host_ =input("Introduce la direccion IP: ")
    port_ = int(input("Introduce puerto: "))
    nick = input ("Nombre de usuario: ")

    nicks = []
    


    def __init__(self, host=host_, port=port_, nickname=nick):
        self.sock = socket.socket()
        self.sock.connect((str(host), int(port)))
        hilo_recv_mensaje = threading.Thread(target=self.recibir)
        hilo_recv_mensaje.daemon = True
        hilo_recv_mensaje.start()
        print('Hilo con PID', os.getpid())
        print('Hilos activos', threading.active_count())
        self.enviarNick(nickname)

        while True:
            msg = input('\nEscriba Texto ? ** Enviar = ENTER ** Abandonar Chat = Q \n')

            if msg != 'Q':
                self.enviar(nickname + ": " + msg)
            else:
                print("*** Adios Majo ***")
                self.sock.close()
                sys.exit()
    
    def recibir(self):
        while True:
            try:
                data = self.sock.recv(32)
                if data:
                    print(pickle.loads(data))
            except:
                pass
    def enviar(self, msg):
        self.sock.send(pickle.dumps(msg))

    def enviarNick(self, nick):
        self.sock.send(pickle.dumps(nick))
c = Cliente()
