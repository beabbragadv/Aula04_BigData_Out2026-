compra = float (input('Valor da compra: '))
cliente_frequente = input('Programa de fidelidade? [S/N]:').lower()[0]
print(cliente_frequente)

if compra > 100 or cliente_frequente == 's':
    print('Recebe Brinde')

else:
    print('Sem brinde')