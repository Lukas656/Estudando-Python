# Ordem de Precedência de Operadores 
#1 () Parentese 
#2 **  potencias
#### Neste caso siga nessa ordem 
#3  * Multiplicação ,  / Divisão , // Divisão inteira ,  % Resto da Divisão
#4 + Soma, - Subtração

# Exemplos:
nome = 'Lucas'
print('Prazer em te conhecer {:=^20}!'.format(nome))
#A mensagem tem um comprimento total de 20 caracteres e o valor da variável
# nome é inserido no centro, preenchido com o caractere de igual (=) repetido à esquerda
# e à direita para atingir o comprimento desejado.

n1 = int(input('Um Valor: '))
n2 = int(input('Segundo Valor: '))

soma = n1 + n2
subitracao = n1 - n2
multiplicacao = n1 * n2
divisao =  n1 / n2
divInteira = n1 // n2
potencia = n1 ** n2

print('A Soma é: {}, \n Sua subtração é {}, \n  multiplicação: {}'.format(soma, subitracao, multiplicacao)) # Ultilizei o \n apenas para quebrar linha
print('Divisão: {:.3f}, Divisão inteira: {}, Potencia: {}'.format(divisao, divInteira, potencia)) # Acrecentei o Divisão: {:.3f} para deixar 3 casas dps da , ex (1.3333333333333333) para 1.333


