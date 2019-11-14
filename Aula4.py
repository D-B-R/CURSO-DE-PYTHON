#escreva um programa que leia um valor em metros e converta para centimetros e milimetros


n1= float(input('Digite o valor a ser convertido\n'))
n2=n1*100
n3=n1*1000
print('o valor de {:.0f} convertido em centimentros é de {:.0f} centimetros e o valor de {:.0f} convertido em milimetros'
      'é de {:.0f} milimetros'.format(n1,n2,n1,n3))