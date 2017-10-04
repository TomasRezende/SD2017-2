import sys

sys.path.append('gen-py')

from grafodb import Operacoes
from grafodb.ttypes import Vertice, Aresta, Grafo
from handler import Handler

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer



class Server(object):
    def __init__(self):
        pass

    def run(self, porta = 9090):
        handler = Handler()
        processor = Operacoes.Processor(handler)
        transport = TSocket.TServerSocket(port=porta)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()

        server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)
        server.serve()


if __name__ == '__main__':
    print("Servidor Online!")
    server = Server()
    server.run()