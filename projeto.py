print('Produtos terão 5% de desconto sobre o seu valor.')
valor = float(input('Digite o valor do produto, R$:'))
desconto = (5 / 100) * valor
total = valor - desconto
print('O total de desconto sobre o valor de R${:.2f} foi de {:.2f} e seu valor final é de {:.2f}'.format(valor, desconto, total))
