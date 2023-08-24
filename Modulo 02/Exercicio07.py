space = '='
print('Exercicios {:=^50}'.format(space))


# Crie um algoritmo que leia um numero e mostre 
# o seu dobro, triplo, e raiz quadrada.
num = int(input('Digite o Numero: '))
dobro = num*2
triplo = num*3
raiz = pow(num , (1/2))

print('Exercicio 02 {:=^50}'.format(space))
print('Numero Escolhido: {} \n Seu Dobro é {} \n Seu Triplo é {}, \n Sua Raiz Quadrada é: {:.2f}  '.format(num, dobro, triplo, raiz )) # Calcula a raiz quadrada elevando o número a 0.5  e {:.2f} foi usado para deixar 2 digitos dps da virgula

