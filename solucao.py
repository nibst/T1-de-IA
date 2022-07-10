from  heapqModified import heappop,heappush
import time
from Tree import Tree
class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado, pai, acao, custo):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        

def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """

    transicoes = []
    j = 0
    for i in estado:
        if i == "_":
            casa = j
            break
        j = j + 1
    if casa < 6: #move para baixo
        estado_novo = list(estado)
        estado_novo[casa+3], estado_novo[casa] = estado_novo[casa], estado_novo[casa+3]
        estado_novo = ''.join(estado_novo)
        tupla = ("abaixo", estado_novo)
        transicoes.append(tupla)
    if (casa > 2): #move para cima
        estado_novo = list(estado)
        estado_novo[casa-3], estado_novo[casa] = estado_novo[casa], estado_novo[casa-3]
        estado_novo = ''.join(estado_novo)
        tupla = ("acima", estado_novo)
        transicoes.append(tupla)
    if (casa % 3 == 0) or (casa % 3 == 1): #move para direita
        estado_novo = list(estado)
        estado_novo[casa+1], estado_novo[casa] = estado_novo[casa], estado_novo[casa+1]
        estado_novo = ''.join(estado_novo)
        tupla = ("direita", estado_novo)
        transicoes.append(tupla)
    if (casa % 3 == 2) or (casa % 3 == 1): #move para esquerda
        estado_novo = list(estado)
        estado_novo[casa-1], estado_novo[casa] = estado_novo[casa], estado_novo[casa-1]
        estado_novo = ''.join(estado_novo)
        tupla = ("esquerda", estado_novo)
        transicoes.append(tupla)
    return transicoes


def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    nodos = []
    for s in sucessor(nodo.estado):
        nodos.append(Nodo(s[1], nodo, s[0], nodo.custo + 1))
    return nodos


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    objetivo = '12345678_'
    
    raiz = Nodo(estado,None,None,0)
    
    X = []
    F = []
    custo_biased = soma_manhattan(raiz.estado) + raiz.custo
    heappush(F,(custo_biased,raiz))
    sucessores = expande(raiz)
    count = 0
    estados_explorados = Tree()
    start = time.time()
    while F:        
        explorado=heappop(F)
        if estados_explorados.insere(explorado[1].estado):
            X.append(explorado)
            if explorado[1].estado == objetivo:
                nodo = explorado[1]
                caminho_inverso =[]
                while nodo.pai != None:
                    caminho_inverso.append(nodo)
                    nodo = nodo.pai
                caminho_certo = []
                for i in range (len(caminho_inverso)):
                    caminho_certo.append(caminho_inverso.pop())
                end = time.time()
                print(end-start)
                return caminho_certo
            sucessores = expande(explorado[1])
            for sucessor in sucessores:
                
                custo_biased  = soma_manhattan(sucessor.estado) + sucessor.custo
                
                heappush(F,(custo_biased,sucessor))
                
    end = time.time()
    print(end-start)
    return None
        
    """
    busca_grafo(s):

    X ← {}

    F ← {new Node(s)} 

    loop:

    se F = ∅: FALHA

    v ← retira(F)

    se v é o objetivo: retornar caminho s-v

    se v ∉ X:

        Insere v em X 

        Cria Node pra cada vizinho de v e insere em F
    """
    

def soma_manhattan(estado):
    matriz_estado = []
    soma_manhattan = 0
    #transformar em matriz
    linha = []
    for nmr_casa,peca in enumerate(estado):
        linha.append(peca)
        if (nmr_casa + 1) % 3 == 0:
            matriz_estado.append(linha)
            linha = []
    #1 fica na matriz[0][0]
    #2 fica na matriz[0][1]
    #3 fica na matriz[0][2]
    for i in range(3):
        for j in range(3):
            if matriz_estado[i][j] != '_':
                pos = calcula_posicao_objetivo(matriz_estado[i][j])
                soma_manhattan+= abs(pos[0] - i) + abs(pos[1] - j)
    return soma_manhattan

def calcula_posicao_objetivo(peca):
    """
    Returns
    -------
     : Tuple
        tupla com os index i e j que ele deveria ter na posicao objetivo
    """
    numero_peca = int(peca)
    if numero_peca <= 3:
        return (0,numero_peca-1)
    if numero_peca <=6:
        j  = numero_peca % 4
        return(1,j)
    if numero_peca <=9:
        j  = numero_peca % 7
        return(2,j)




