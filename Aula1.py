#crie um algoritmo que leia um número e mostre o seu dobro e o seu , triplo
# e a sua raiz ! SEM O USO DE BIBLIOTECA


n1= int(input('Digete um número!\n'))
n2=n1*2
n3=n1*3
n4=n1**(1/2)
print('O dobro do número  {} é {} e o tripo do número {} é {} e a raiz qualdrada do número {} é {:.0f}'.format(n1,n2,n1,n3,n1,n4))