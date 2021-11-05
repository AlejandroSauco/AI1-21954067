import socket
import threading
import sys
import pickle
import os

class Servidor():
    
    port_ = int(input("Introduce tu puerto: "))

    def __init__(self, host=socket.gethostname(), port=port_):
        self.nicks = []
        self.clientes = []
        self.sock = socket.socket()
        self.sock.bind((str(host), int(port)))
        self.sock.listen(20)
        self.sock.setblocking(False)

        aceptar = threading.Thread(target=self.aceptarC)
        procesar = threading.Thread(target=self.procesarC)


        aceptar.daemon = True
        aceptar.start()

        procesar.daemon = True
        procesar.start()


        while True:
            msg = input('SALIR = Q\n')
            if msg == 'Q':
                print("**** TALOGOO ****")
                self.sock.close()
                sys.exit()
            elif msg == 'p':
                print("Los siguientes usuarios se han conectado: ")
                for i in range(len(self.usuarios)):
                    print(i+1, "-", self.usuarios[i])
            else:
                pass

    def broadcats(self, msg, cliente):
        for c in self.clientes:
            try:
                if c != cliente:
                    c.send(msg)
            except:
                self.clientes.remove(c)
    
    def aceptarC(self):
        while True:
            try:
                conn, addr = self.sock.accept()
                print(f"\nConexion aceptada via {conn}\n")
                conn.setblocking(False)
                self.clientes.append(conn)
            except:
                pass
    def procesarC(self):
        print("Procesamiento de mensajes iniciado")
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c.recv(32)
                        if data:
                            self.broadcast(data, c)
                            if ": " not in pickle.loads(data):
                                print(pickle.loads(data))
                                self.nicks.append(pickle.loads(data))
                            else:
                                print(pickle.loads(data))
                                f = open("u21954067.txt", "a")
                                f.write(pickle.loads(data) + "\n")
                                f.close()
                            print(pickle.loads(data))
                    except:
                        pass
s = Servidor()