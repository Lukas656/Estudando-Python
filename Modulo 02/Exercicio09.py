# Escreva um programa que leia o valor em metros
# e o exiba convertido em centimetros e milimetros

medida = float(input('Defina uma distancia em Metros: '))
cm = medida * 100
mm = medida * 1000

print('A medida de {} corresponde de {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))


