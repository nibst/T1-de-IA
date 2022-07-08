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
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

