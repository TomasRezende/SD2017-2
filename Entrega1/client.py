import sys
import queue
import threading

sys.path.append('gen-py')

from grafodb import Operacoes
from grafodb.ttypes import Vertice, Aresta, Grafo

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

q = queue.Queue()

def clienteUm(host = 'localhost', porta = 9090):
    print('Cliente 1 teste 1')
    # Instancia o Socket
    transport = TSocket.TSocket(host, porta)
    print('Cliente 1 teste 2')
    # Buffering do Socket.
    transport = TTransport.TBufferedTransport(transport)
    print('Cliente 1 teste 3')
    # Adiciona um Protocolo ao Socket
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    print('Cliente 1 teste 4')
    # Cria um cliente para se conectar
    cliente = Operacoes.Client(protocol)
    print('Cliente 1 teste 5')
    # Fazendo a coexão com o servidor
    transport.open()
    print('Cliente 1 teste 6')

    #cliente.removeVertice(1)
    #print(cliente.vizinhos(1))
    #cliente.criaVertice(Vertice(7,1,10,"sete"))
    #cliente.criaAresta(1,6,10,True,"aresta8")
    #cliente.removeAresta(4,5)

    q.put("Thread 1 finalizada")

def clienteDois( host = 'localhost', porta = 9090):
    print('Cliente 2 teste 1')
    # Instancia o Socket
    transport = TSocket.TSocket(host, porta)
    print('Cliente 2 teste 2')
    # Buffering do Socket.
    transport = TTransport.TBufferedTransport(transport)
    print('Cliente 2 teste 3')
    # Adiciona um Protocolo ao Socket
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    print('Cliente 2 teste 4')
    # Cria um cliente para se conectar
    cliente = Operacoes.Client(protocol)
    print('Cliente 2 teste 5')
    # Fazendo a coexão com o servidor
    transport.open()
    print('Cliente 2 teste 6')
    #cliente.removeVertice(1)
    #print(cliente.vizinhos(1))
    cliente.criaVertice(Vertice(7,1,10,"sete"))
    #cliente.criaAresta(1,6,10,True,"aresta8")
    #cliente.removeAresta(4,5)

    q.put("Thread 2 finalizada")


class Client:
    def __init__(self):
        pass

    def run(self):
        t1 = threading.Thread(target=clienteUm)
        t2 = threading.Thread(target=clienteDois)
        t1.daemon = True
        t2.daemon = True
        t1.start()
        print('startando t2')
        t2.start()

        q.get()

if __name__ == "__main__":
    client = Client()
    client.run()