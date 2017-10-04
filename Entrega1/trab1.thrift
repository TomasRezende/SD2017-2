namespace go grafodb
namespace py grafodb

typedef i32 int

exception ElementNotFoundException{ }

struct Vertice {
            1:int id,
            2:int cor,
            3:double peso,
            4:string descricao
}

struct Aresta {
            1:Vertice verticeUm,
            2:Vertice verticeDois,
            3:double peso,
            4:bool bidirecional,
            5:string descricao
}

struct Grafo {
            1:list<Vertice> Vertices,
            2:list<Aresta> Arestas,
}

service Operacoes {

        void criaVertice(1:Vertice v),
        void criaAresta(1:int verticeUm, 2:int verticeDois, 3:double peso, 4:bool bidirecional, 5:string descricao),
        void atualizaVertice(1:Vertice v),
        void atualizaAresta(1:int verticeUm, 2:int verticeDois, 3:double peso, 4:bool bidirecional, 5:string descricao),
        Vertice leVertice(1:int Id)  throws (1:ElementNotFoundException e),
        Aresta leAresta(1:int verticeUm, 2:int verticeDois)  throws (1:ElementNotFoundException e),
        void removeVertice(1:int id),
        void removeAresta(1:int verticeUm, 2:int verticeDois),
        list<Aresta> arestasDoVertice(1:int id)  throws (1:ElementNotFoundException e),
        list<Vertice> vizinhos(1:int id)  throws (1:ElementNotFoundException e)
}
