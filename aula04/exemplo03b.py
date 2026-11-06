pontos = int(input('informe os pontos: '))

if pontos >= 100:
    pontos = pontos + 10
    print(f'Excelente! Você tem {pontos} agora!')

if pontos >= 50:
    pontos = pontos + 5
    print(f'Bom desempenho! Você tem {pontos} agora')

else:
    print(f' Não desanime, você está començando. Seus pontos: {pontos}')