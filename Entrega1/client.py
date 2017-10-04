import sys
import queue
import threading
import argparse

sys.path.append('gen-py')

from grafodb import Operacoes
from grafodb.ttypes import Vertice, Aresta, Grafo

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


try:
    par = argparse.ArgumentParser()
    par.add_argument("-p", "--porta", help="Porta", required=True)
    par.add_argument("-o", "--host", help="Host",  required=True)
    args = par.parse_args()
    Porta = args.porta
    Host = args.host
except Exception as e:
    print(e)
    exit()

def clienteUm(host = 'localhost', porta = 9090):
    #print('Cliente 1 teste 1')
    # Instancia o Socket
    transport = TSocket.TSocket(host, porta)
    #print('Cliente 1 teste 2')
    # Buffering do Socket.
    transport = TTransport.TBufferedTransport(transport)
    #print('Cliente 1 teste 3')
    # Adiciona um Protocolo ao Socket
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    #print('Cliente 1 teste 4')
    # Cria um cliente para se conectar
    cliente = Operacoes.Client(protocol)
    print('Iniciando cliente 1...')
    # Fazendo a coexão com o servidor
    transport.open()

    #cliente.removeVertice(1)
    print(cliente.vizinhos(2))
    #cliente.criaVertice(Vertice(7,1,10,"sete"))
    #cliente.criaAresta(1,6,10,True,"aresta8")
    #cliente.removeAresta(4,5)

def clienteDois( host = 'localhost', porta = 9090):
    #print('Cliente 2 teste 1')
    # Instancia o Socket
    transport = TSocket.TSocket(host, porta)
    #print('Cliente 2 teste 2')
    # Buffering do Socket.
    transport = TTransport.TBufferedTransport(transport)
    #print('Cliente 2 teste 3')
    # Adiciona um Protocolo ao Socket
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    #print('Cliente 2 teste 4')
    # Cria um cliente para se conectar
    cliente = Operacoes.Client(protocol)
    print('Iniciando cliente 2...')
    # Fazendo a coexão com o servidor
    transport.open()

    #cliente.removeVertice(1)
    print(cliente.vizinhos(2))
    #cliente.criaVertice(Vertice(7,1,10,"sete"))
    #cliente.criaAresta(1,6,10,True,"aresta8")
    #cliente.removeAresta(4,5)


class Client:
    def __init__(self):
        pass
    #target=exec_cms_command, args=(host, host_hash, id_scan)
    def run(self):
        print(Host+" || "+ Porta)
        t1 = threading.Thread(target=clienteUm, args=(Host,Porta))
        t2 = threading.Thread(target=clienteDois, args=(Host,Porta))
        t1.start()
        t2.start()

if __name__ == "__main__":
    client = Client()
    client.run()