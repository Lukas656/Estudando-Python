# Faça um programa que leia um numero inteiro
# e mostre na tela o seu sucessor e seu antecessor.
space = '='
print('Exercicios {:=^50}'.format(space))


num = int(input('Digite o Numero: '))
print('Exercicio 01 {:=^50}'.format(space))

print('O Numero antessesor de {}, é {}, e seu sucessor é {}'.format(num, (num-1), (num+1)))
