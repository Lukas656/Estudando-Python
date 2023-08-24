
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
# e mostre quantos Dólares ela pode comprar.
# considere USS 1,00 = R$ 4,88   
# (Data da cotação do dollar 24/08/2023) pesquese para ter certeza que não mudou

real = float(input('Quanto dinheiro você tem na Carteira: R$'))

dolar = real / 4.88

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real,dolar))