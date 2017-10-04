import sys
sys.path.append('gen-py')

from grafodb.ttypes import Vertice, Aresta, Grafo,  ElementNotFoundException
from threading import Lock

trava = Lock()

def pegaVertice(Id, Vertices):
    for v in Vertices:
        if v.id == Id:
            return v
    return None

def pegaAresta(verticeUm, verticeDois, Arestas):
    for a in Arestas:
            if((a.verticeUm.id == verticeUm and a.verticeDois.id == verticeDois) or (a.verticeUm.id == verticeDois and a.verticeDois.id == verticeUm)):
                return a
    return None

def carregaArq():
    Vertices = []
    Arestas = []

    trava.acquire()
    with open("carga_vertices", "r") as file:
        for line in file:
            line = line.replace("\n","")
            args = line.split(",")
            v = Vertice(int(args[0]), int(args[1]), float(args[2]), args[3])
            Vertices.append(v)

    with(open("carga_arestas","r")) as file:
        for line in file:
            line = line.replace("\n","")
            args = line.split(",")
            verticeUm = pegaVertice(int(args[0]), Vertices)
            verticeDois = pegaVertice(int(args[1]),Vertices)
            if(verticeUm != None and verticeDois != None):
                a = Aresta(verticeUm, verticeDois, float(args[2]), bool(args[3]), args[4])
                Arestas.append(a)


    trava.release()
    return Grafo(Vertices, Arestas)


def verticeToString(v):
    vstring = "\n"
    vstring += str(v.id)+","
    vstring += str(v.cor)+","
    vstring += str(v.peso)+","
    vstring += v.descricao
    return vstring

def arestaToString(a):
    astring = "\n"
    astring += str(a.verticeUm.id)+","
    astring += str(a.verticeDois.id)+","
    astring += str(a.peso)+","
    astring += str(a.bidirecional)+","
    astring += a.descricao
    return astring

def gravaVertice(v):
    with open("carga_vertices","a") as f:
        f.write(verticeToString(v))

def gravaAresta(a):
    with open("carga_arestas", "a") as f:
        f.write(arestaToString(a))

def gravaVertices(Vertices):
    vstring = ""
    for v in Vertices:
        vstring += verticeToString(v)
    with open("carga_vertices", "w") as f:
        f.write(vstring)

def gravaArestas(Arestas):
    astring = ""
    for a in Arestas:
        astring += arestaToString(a)
    with open("carga_arestas", "w") as f:
        f.write(astring)

def gravaArquivo(grafo):
    gravaVertices(grafo.Vertices)
    gravaArestas(grafo.Arestas)


def atualizaVertice(v, grafo):
    Vertices = grafo.Vertices
    verticeAux = []
    existe = False
    for i in range(len(Vertices)):
        if(v.id == Vertices[i].id):
            verticeAux = Vertices[:i]+Vertices[i+1:]
            verticeAux.append(v)
            existe = True
            break

    if(existe):
        writeVertex(verticeAux)

def atualizaAresta(a, Arestas):
    arestasAux = []
    existe = False
    for i in range(len(Arestas)):
        if((Arestas[i].verticeUm.id == a.verticeUm.id and Arestas[i].verticeDois.id == a.verticeDois.id) or (Arestas[i].verticeDois.id == a.verticeUm.id and Arestas[i].verticeUm.id == a.verticeDois.id)):
            arestaAux = Arestas[:i] + Arestas[i+1:]
            arestaAux.append(a)
            existe = True
            break
    if(existe):
        writeEdges(arestaAux)

def apagaVertice(Id, grafo):
    lista_vertices = grafo.Vertices
    lista_arestas = grafo.Arestas
    verticeAux = []
    arestaAux = []
    for i in range(len(lista_vertices)):
        if(lista_vertices[i].id == Id):
            verticeAux = lista_vertices[:i]+lista_vertices[i+1:]

    for a in lista_arestas:
        if(a.verticeUm.id != Id and a.verticeDois.id != Id):
            arestaAux.append(a)
    gravaArquivo(Grafo(verticeAux, arestaAux))

def apagaAresta(verticeUm, verticeDois, Arestas):
    arestaAux = []
    for a in Arestas:
        if(a.verticeUm.id != verticeUm or a.verticeDois.id != verticeDois):
            if(a.bidirecional):
                if(a.verticeDois.id != verticeUm or a.verticeUm.id != verticeDois):
                    arestaAux.append(a)
            else:
                arestaAux.append(a)
    gravaArestas(arestaAux)


def pegaArestasDoVertice(v, Arestas):
    arestaAux = []
    for a in Arestas:
        if(v.id == a.verticeUm.id or v.id == a.verticeDois.id):
            arestaAux.append(a)

    return arestaAux

def pegaVizinhos(v, Arestas):
    arestaAux = []
    for a in Arestas:
        if(v.id == a.verticeUm.id):
            arestaAux.append(a.verticeDois)
        elif(v.id == a.verticeDois.id):
            arestaAux.append(a.verticeUm)
    return arestaAux

class Handler:

    def __init__(self):
        pass

    def criaVertice(self, v):
        grafo = carregaArq()
        trava.acquire()
        if(pegaVertice(v.id, grafo.Vertices) == None):
            print('Gravando o vertice no arquivo...')
            gravaVertice(v)
        else:
            print("Vertice ja existe")
        trava.release()

    def criaAresta(self,  verticeUm, verticeDois, peso, bidirecional, descricao):
        grafo = carregaArq()
        trava.acquire()
        v1 = pegaVertice(verticeUm, grafo.Vertices)
        v2 = pegaVertice(verticeDois, grafo.Vertices)
        a = pegaAresta(v1, v2, grafo.Arestas)
        if(v1 != None and v2 != None and a == None ):
            gravaAresta(Aresta(v1, v2, peso, bidirecional, descricao))
        trava.release()

    def leVertice(self, Id):
        grafo = carregaArq()
        v = pegaVertice(Id, grafo.Vertices)
        if(v != None):
            return v
        else:
            erro = ElementNotFoundException()
            raise erro
            
    def leAresta(self, verticeUm, verticeDois):
        grafo = carregaArq()
        a = searchEdge(verticeUm, verticeDois, grafo.Arestas)
        if (a != None):
            return a
        else:
            erro = ElementNotFoundException()
            raise erro

    def removeVertice(self, Id):
        grafo = carregaArq()
        apagaVertice(Id, grafo)


    def removeAresta(self, verticeUm, verticeDois):
        grafo = carregaArq()
        apagaAresta(verticeUm, verticeDois, grafo.Arestas)


    def arestasDoVertice(self, vertice):
        grafo = carregaArq()
        v = pegaVertice(vertice, grafo.Vertices)
        if(v != None):
            return pegaArestasDoVertice(v, grafo.Arestas)
        else:
            erro = ElementNotFoundException()
            raise erro

    def vizinhos(self, vertice):
        grafo = carregaArq()
        v = pegaVertice(vertice, grafo.Vertices)
        if(v != None):
            return pegaVizinhos(v, grafo.Arestas)
        else:
            erro = ElementNotFoundException()
            raise erro