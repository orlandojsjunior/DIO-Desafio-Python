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

8 - A primeira linha usa a função input para ler o texto do usuário e armazená-lo na variável T
9 - A segunda linha usa a função len para obter o tamanho do texto em caracteres e compara com o 
limite de 140 usando o operador <=.
10 -A terceira linha usa a função print para imprimir a palavra “TWEET” se a condição for 
verdadeira, ou seja, se o texto tiver até 140 caracteres.
11 - A quarta linha usa a palavra-chave else para indicar o que fazer se a condição for falsa, ou 
seja, se o texto tiver mais de 140 caracteres.
12 - A quinta linha usa a função print para imprimir a palavra “MUTE” se a condição for falsa.

'''

