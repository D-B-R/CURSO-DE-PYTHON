#faça um algoritmo que leia o preço de um produto e mostre o preço com desconto de 5%


n1=float(input('Digite o valor do produto\n'))
n2=n1*0.05
n3=n1-n2
print('o valor do produto com 5% de desconto é de R${:.2f}'.format(n3))
print('o valor de desconto foi de R${:.2f}'.format(n2))