import ctypes

# Serve para definir um número para qualquer tipo de dado, podendo ser objeto, lista, etc.
def numero(valor):
    return ctypes.c_int.from_address(id(valor)).value

# Define tipo de dados Set através de uma classe.
class meuSet:
    # Recebe um tamanho (quantidade de dados que aceita) e monta uma matriz baseado nesse tamanho, com valores None.
    def __init__(self, tamanho):
        self.tamanho = tamanho 
        self.matriz = [None] * tamanho
        self.elementos_inseridos = 0
    # Aqui lista os valores preenchidos na matriz
    def listar(self):
        for i in range(self.tamanho):
            # Lista tudo, lista, objeto, inteiro, string e os diabo.
            if self.matriz[i] is not None:
                print(self.matriz[i]) #tenho que entender ainda
            # Agora se não tem nada, mostra Vazion
            else:
                print('VAZIO')

    # Aqui retorna a chave da nossa hash, ou seja, em que posição vai gravar o valor
    # Esse cálculo é dado pelo resto da divisão da chave pelo tamanho
    # Para um caso base, vamos definir todo o valor em chave como inteiro, pois não tenho capacidade intelectual caso isso seja uma lista ou objeto agora no momento
    def hash(self, chave):
        posicao = numero(chave) % self.tamanho
        return posicao
    
    # Aqui é a função para inserir. Coloco um valor a uma posição da matriz definida nesse tipo de dado
    def inserir(self, chave):
        if self.elementos_inseridos >= self.tamanho:
            # A tabela está cheia, você pode lançar uma exceção ou retornar False
            print("A tabela está cheia, não é possível inserir mais elementos.")
            # Ou
            # return False
        # Calculo uma posição
        posicao = self.hash(chave)
        # Vejo se já está preenchida ou se está removida. Se está removida, eu tenho que gerar uma nova, pelo resto da divisão do hash + 1, dessa vez.
        while self.matriz[posicao] is not None:
            posicao = posicao + 1
            posicao = posicao % self.tamanho
        # A posição que encontrar pra esse diabo é onde eu armazeno o meu valor
        self.matriz[posicao] = chave
        self.elementos_inseridos += 1
        
    # Aqui tem que apagar. Outra desgraça, mas parecido com inserir
    def remover(self, chave):
        # Calculo a posição da minha chave que desejo excluir
        posicao = self.hash(chave)
        # Enquanto tem valor nessa posição...
        while self.matriz[posicao] is not None:
            # Vejo se o valor confere...
            if self.matriz[posicao] == chave:
                # Se confere eu vou armazenar nesse valor REMOVIDO para avisar que não tem mais
                self.matriz[posicao] = None
                # Retorno True pois removeu
                return True
            # Agora se o valor não confere...
            else:
                # Calculo a próxima posição de hash possível para percorrer minha tabela
                posicao = posicao + 1
                posicao = posicao % self.tamanho
        # Se o corno do usuário simplesmente não atinou a inserir um valor decente para remover...
        # ...retorno False para avisar o abençoado
        return False
    
    #
    def buscar(self, chave):
        # Calculo a posição do meu hash
        posicao = self.hash(chave)
        # Enquanto tem valor nessa posição...
        while self.matriz[posicao] is not None:
            # Vejo se o valor confere...
            if self.matriz[posicao] == chave:
                # Valor confere? Show, retorna pro abençoado
                return self.matriz[posicao]
            # Agora se o valor não confere...
            else:
                # Calculo a próxima posição de hash possível para percorrer minha tabela
                posicao = posicao + 1
                posicao = posicao % self.tamanho
        # Se o corno do usuário simplesmente não atinou a inserir um valor decente para buscar...
        # ...retorno None porque o usuário é um imecíl
        return None
    
    # Aqui faz a união dos elementos de um outro conjunto tipo meuSet enviado por parâmetro
    def uniao(self, matriz):
        # Soma os tamanhos
        self.tamanho = self.tamanho + matriz.tamanho
        # Junta as matrizes
        self.matriz = [*self.matriz, *matriz.matriz]

    # Aqui faz a intersecção, retornando os valores comuns entre o objeto tipo meuSet com outro objeto do tipo meuSet
    def interseccao(self, matriz):
        # Desempacota os valores das matrizes e adiciona em variáveis a e b
        a = [*self.matriz]
        b = [*matriz.matriz]
        # Armazena a intersecção em uma matriz nova
        c = a.intersection(b)
        # Depois retorna a intersecção, adaptado ao tipo de dado meuSet
        return meuSet(len(c),[c])
    
    # Aqui retorna a diferença entre um tipo de dado meuSet para outro
    def diferenca(self, matriz):
        # Aqui ele desempacote a matriz a
        a = [*matriz.matriz]
        # Armazena a intersec
        b = [*self.intersection(matriz).matriz]
        for elemento in b:
            a.remove(elemento)
        return meuSet(len(a),[a])
        
        
def main():
    rodando = True

    set1 = meuSet(10)
    set1.inserir(1)
    set1.inserir('abc')
    set1.inserir([1,2])
    set1.inserir(True)
    set1.inserir(False)

    set1.listar()

    set2 = meuSet(5)
    set2.inserir(2)
    set2.inserir('cde')
    set2.inserir([3,4])
    set2.inserir('Funciona')
    set2.inserir('Desgraça')
    set2.inserir('Desgraçaw')

    set2.listar()

main()
    
    
