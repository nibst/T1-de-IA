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
    possiveis_movimentos = ['acima','abaixo','esquerda','direita']
    for movimento in possiveis_movimentos:
        transicao = mover_vazio(movimento,estado)
        if transicao: #se nao for Nonne
            transicoes.append(transicao)
    return transicoes
    
    
    
            

def mover_vazio(movimento,estado):
    """
    Move o espaço vazio com o movimento especificado no parametro movimento

    Parameters
    ----------
    `movimento`: str 
        especifica o movimento a ser feito
    `estado` : str 
        estado que será aplicado o movimento

    Returns
    -------
     : None
        caso seja inválido o movimento
     : Tuple
        tupla (movimento,novo_estado) caso seja movimento válido
    """    
    offset_dict= {}
    offset_dict['acima'] = -3
    offset_dict['abaixo'] = 3
    offset_dict['esquerda'] = -1
    offset_dict['direita'] = 1
    

    novo_estado = list(estado)
    limite_sup = 8
    limite_inf = 0
    peca_vazia = '_'
    offset = offset_dict[movimento]
    for count,peca in enumerate(estado):
        if peca == peca_vazia:
            if count + offset > limite_sup or count + offset < limite_inf:
                return None
            else:
                troca = estado[count+offset]
                novo_estado[count] = troca
                novo_estado[count+offset] = peca_vazia 
                novo_estado = ''.join(novo_estado) #transforam em string para retornar
                return (movimento,novo_estado)

def abaixo(estado):
    """
    retorna tupla ('abaixo', novo_estado) caso seja possivel ir para baixo
    retorna None caso não seja possível
    """
    novo_estado = list(estado)
    upper_bound = 8
    peca_vazia = '_'
    offset = 3
    for count,peca in enumerate(estado):
        if peca == peca_vazia:
            if count + offset > upper_bound:
                return None
            else:
                troca = estado[count+offset]
                novo_estado[count] = troca
                novo_estado[count+offset] = peca_vazia 
                novo_estado = ''.join(novo_estado) #transforam em string
                return ('abaixo',novo_estado)


def acima(estado):
    """
    retorna tupla ('acima', novo_estado) caso seja possivel ir para baixo
    retorna None caso não seja possível
    """
    novo_estado = list(estado)
    lower_bound = 0
    peca_vazia = '_'
    offset = -3
    for count,peca in enumerate(estado):
        if peca == peca_vazia:
            if count + offset < lower_bound:
                return None
            else:
                troca = estado[count+offset]
                novo_estado[count] = troca
                novo_estado[count+offset] = peca_vazia 
                novo_estado = ''.join(novo_estado) #transforam em string
                return ('acima',novo_estado)

def esquerda(estado):
    """
    retorna tupla ('abaixo', novo_estado) caso seja possivel ir para baixo
    retorna None caso não seja possível
    """
    novo_estado = list(estado)
    lower_bound = 0
    peca_vazia = '_'
    offset = -1
    for count,peca in enumerate(estado):
        if peca == peca_vazia:
            if count + offset < lower_bound:
                return None
            else:
                troca = estado[count+offset]
                novo_estado[count] = troca #peça que vai para o espaço vazio
                novo_estado[count+offset] = peca_vazia #espaco vazio fica no lugar da peca
                novo_estado = ''.join(novo_estado) #transforam em string
                return ('esquerda',novo_estado)
def direita(estado):
    """
    retorna tupla ('abaixo', novo_estado) caso seja possivel ir para baixo
    retorna None caso não seja possível
    """
    novo_estado = list(estado)
    upper_bound = 8
    peca_vazia = '_'
    offset = 1
    for count,peca in enumerate(estado):
        if peca == peca_vazia:
            if count + offset > upper_bound:
                return None
            else:
                troca = estado[count+offset]
                novo_estado[count] = troca #peça que vai para o espaço vazio
                novo_estado[count+offset] = peca_vazia #espaco vazio fica no lugar da peca
                novo_estado = ''.join(novo_estado) #transforam em string
                return ('direita',novo_estado)
def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


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
