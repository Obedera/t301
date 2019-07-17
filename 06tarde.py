salario = float(input('Digite seu salario: '))
emprestimo = float(input('Digite o valor desejado para emprestimo: '))

if ((salario>1000) and (emprestimo>2000 and emprestimo<salario*15)):
    print('emprestimo aprovado')
else:
    print('emprestimo negado')

def media(*valores):
    sum = 0
    for n in valores[0]:
        sum += float(n)
    return sum/len(valores[0])

valor = None
lista = []

while True:
    valor = input('Quais valores para média digite sair para para : ')
    if valor == 'sair':
        break
    lista.append(valor)

print('Sua média é ', media(lista))
