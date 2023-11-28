''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
T = input()
if len(T) <= 140:
  print("TWEET")
else:
  print("MUTE")


''' 
  T Ler a variável de entrada e verificar se ela possui mais ou menos que 140 caracteres.
  Se for maior imprima "MUTE" e se for igual ou menor imprima "TWEET".

'''

'''

Desafio:

O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua tarefa.

Entrada:
A entrada é uma linha de texto T (1 ≤ |T| ≤ 500).

Saída:
A saída é dada em uma única linha. Ela deve ser "TWEET" (sem as aspas) se a linha de texto T tem até 140 caracteres. Se T tem mais de 140 caracteres, a saída deve ser "MUTE".

 
Exemplo de Entrada:
	
RT @TheEllenShow: If only Bradley's arm was longer. Best photo ever. #oscars pic.twitter.com/C9U5NOtGap

Exemplo de Saída:
TWEET

'''

'''
Drescrição do Codigo:

8 - A primeira linha usa a função input para ler o texto do usuário e armazená-lo na variável T
9 - A segunda linha usa a função len para obter o tamanho do texto em caracteres e compara com o 
limite de 140 usando o operador <=.
10 -A terceira linha usa a função print para imprimir a palavra “TWEET” se a condição for 
verdadeira, ou seja, se o texto tiver até 140 caracteres.
11 - A quarta linha usa a palavra-chave else para indicar o que fazer se a condição for falsa, ou 
seja, se o texto tiver mais de 140 caracteres.
12 - A quinta linha usa a função print para imprimir a palavra “MUTE” se a condição for falsa.

'''

