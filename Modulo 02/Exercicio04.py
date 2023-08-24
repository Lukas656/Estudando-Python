algo = input('Digite Algo: ') # se não definir como int, float ou bool ele por padrão virá string idependente do que digitar 

print('o tipo primitivo desse valor é: ',type(algo)) # Aqui vemos que o type() mostra o tiipo primitivo do input
print('Só tem espaços? ', algo.isspace()) # Verifica se Digitei algo ou só espaçei
print('É numérico? ', algo.isnumeric()) # Verifica se é um numero 
print('É alfabético? ', algo.isalpha()) # Verifica se é uma letra 
print('É AlfaNumérico? ', algo.isalnum()) # Verifica se Contem Numeros e letras
print('Letras Maiusculas? ', algo.isupper()) # Verifica se Esta escrito em letras Maiusculas / Tem que estar todas as letras 
print('Letras Minusculas? ', algo.islower()) # Verifica se Esta escrito em letras Minusculas / Tem que estar todas as letras
print('Letras Capitalizada? ', algo.istitle()) # Verifica se Está com a primeira letra maiuscula
# são caracteres ASCII (American Standard Code for Information Interchange).
# O ASCII é um conjunto de caracteres que inclui letras maiúsculas e minúsculas,
# dígitos numéricos e uma variedade de caracteres especiais, como pontuação e símbolos.
print('Contem Caracteres Especiais? ', algo.isascii()) # Verifica se há caracteres especiais comoo (! # $ % ?...) Porem Acentuações como (á ,é ,í ,ã, õ...) retornarão False
