meuCartão = int (input('Digite o número do cartão de credito: '))

cartãoLido = 1
encontreiMeuCartãoNaLista = False 

while cartãoLido != 0and not encontreiMeuCartãoNaLista:
    cartãoLido = int (input('Digite o número do próximo cartão de credito: '))
    if cartãoLido == meuCartão:
        encontreiMeuCartãoNaLista = True

if encontreiMeuCartãoNaLista:
    print('sua tia é minha, seu cartão tbm!')

else:
    print ('WTF? cade meu cartão ')
