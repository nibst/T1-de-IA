

class Tree():
    def __init__(self):
        self.raiz = {}


    def insere(self,estado):
        """
        Retornar True se inseriu, retorna False se o estado ja estava na arvore
        """
        nodo = self.raiz
        is_new = False
        for char in estado:
            if char in nodo:
                nodo = nodo[char]
            else:   
                nodo[char] = {} #criad nodo
                nodo = nodo[char] #entra no nodo criado
                is_new = True
        return is_new