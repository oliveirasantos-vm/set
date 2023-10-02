# set
Implementar as operações do tipo de dados abstratos Set, utilizando alguma estrutura de dados que permita a sua implementação de forma eficiente.


Escolhemos usar hashtable como estrutura de dados por ser uma constante e trazendo mais eficiência. Conforme analisado em aula seu tempo de execução para consulta, inserção inicial, no meio e final sempre será O(1) esperado sempre no melhor caso. 


Hash tables são estruturas de dados que vão permitir que seja criado uma lista de valores pareados, podendo então recuperar determinado valor usando a respectiva chave para aquele valor. 


Para definir a chave da nossa Hash, utilizamos a tabela ASCII. Implementamos uma função chamada converte_int, que recebe um valor qualquer como parâmetro, e esse valor é concatenado com o seu tipo (Exemplo: [<class 'str'>,'Hello World']) formando uma nova string, que é percorrida e convertida para uma sequência de números que representa o inteiro da tabela ASCII. Essa sequência é convertida para inteiro e é calculado o resto da divisão da nossa tabela ASCII, para descobrir a posição.
