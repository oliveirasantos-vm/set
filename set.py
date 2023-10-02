
class Hash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
        self.quantidade = 0
    
    def converte_int(self, valor):
        str_valor = f'[{type(valor)},{valor}]'
        sequencia_ascii = ''
        for caracter in str_valor:
            sequencia_ascii = sequencia_ascii + str(ord(caracter))
        return int(sequencia_ascii)

    def calcula_indice(self, valor):
        return self.converte_int(valor) % self.tamanho
    
    def listar(self):
        for i in range(self.tamanho):
            if self.tabela[i] is not None:
                print(f'{type(self.tabela[i])} = {self.tabela[i]}')
            else:
                print(None)
        return

    def inserir(self, valor):
        indice = self.calcula_indice(valor)
        if self.quantidade < self.tamanho:
            while self.tabela[indice] is not None:
                if self.tabela[indice] == valor and type(self.tabela[indice]) == type(valor):
                    return self.tabela[indice]
                indice = indice + 1
                indice = indice % self.tamanho

            self.tabela[indice] = valor
            self.quantidade = self.quantidade + 1
            return self.tabela[indice] 
        else:
            return None

    def remover(self, valor):
        indice = self.calcula_indice(valor)
        while self.tabela[indice] is not None:
            if self.tabela[indice] == valor and type(self.tabela[indice]) == type(valor):
                self.tabela[indice] = None
                self.quantidade = self.quantidade - 1
                return True
            else:
                indice = indice + 1
                indice = indice % self.tamanho
        return False
    
    def buscar(self, valor):
        indice = self.calcula_indice(valor)
        while self.tabela[indice] is not None:
            if self.tabela[indice] == valor and type(self.tabela[indice]) == type(valor):
                return self.tabela[indice]
            else:
                indice = indice + 1
                indice = indice % self.tamanho
        return None
    
    def interseccao(self, outro_hash):
        conjunto_a = [*self.tabela]
        conjunto_b = [*outro_hash.tabela]

        interseccao_ab = []

        for elemento_a in conjunto_a:
            for elemento_b in conjunto_b:
                if elemento_a == elemento_b and type(elemento_a) == type(elemento_b):
                    interseccao_ab.append(elemento_a)
        
        novo_hash = Hash(len(interseccao_ab))

        for elemento_ab in interseccao_ab:
            novo_hash.inserir(elemento_ab)

        return novo_hash

    def uniao(self, outro_hash):
        conjunto_a = [*self.tabela]
        conjunto_b = [*outro_hash.tabela]

        uniao_ab = conjunto_a

        for elemento_b in conjunto_b:
            if elemento_b not in conjunto_a:
                uniao_ab.append(elemento_b)

        novo_hash = Hash(self.tamanho + outro_hash.tamanho)

        for elemento_ab in uniao_ab:
            novo_hash.inserir(elemento_ab)

        return novo_hash

    def diferenca(self, outro_hash):
        uniao_ab = self.uniao(outro_hash)
        interseccao_ab = self.interseccao(outro_hash)

        conjunto_uniao_ab = [*uniao_ab.tabela]
        conjunto_interseccao_ab = [*interseccao_ab.tabela]

        diferenca_ab = []

        for elemento_uniao_ab in conjunto_uniao_ab:
            for elemento_interseccao_ab in conjunto_interseccao_ab:
                if not (elemento_uniao_ab == elemento_interseccao_ab and type(elemento_uniao_ab) == type(elemento_interseccao_ab)):
                    diferenca_ab.append(elemento_uniao_ab)

        novo_hash = Hash(len(diferenca_ab))

        for elemento_ab in diferenca_ab:
            novo_hash.inserir(elemento_ab)

        return novo_hash
        
def main():

    set_a = Hash(10)
    set_a.inserir(1)
    set_a.inserir('abc')
    set_a.inserir([1,2])
    set_a.inserir(True)
    set_a.inserir(False)
    set_a.inserir(False)
    set_a.inserir('False')
    

    print("--------Set A--------")
    set_a.listar()

    set_b = Hash(5)
    set_b.inserir(1)
    set_b.inserir('cde')
    set_b.inserir([3,4])
    set_b.inserir('fgh')
    set_b.inserir('ijk')
    set_b.inserir('lmn')

    print("--------Set B--------")
    set_b.listar()

    interseccao_ab = set_a.interseccao(set_b)
    print("---Intersecção A B---")
    interseccao_ab.listar()

    uniao_ab = set_a.uniao(set_b)
    print("------União A B------")
    uniao_ab.listar()

    diferenca_ab = set_a.diferenca(set_b)
    print("----Diferença A B----")
    diferenca_ab.listar()

    set_a.remover(2)
    set_a.remover('abc')
    print("Removido 2 e abc de set a")
    print("--------Set A--------")
    set_a.listar()

    print(f'Resultado da busca por 1 no set_a: {set_a.buscar(1)}')
    print(f'Resultado da busca por 999 no set_a: {set_a.buscar(999)}')

main()