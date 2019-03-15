numero = int(input('insira um número inteiro: '))
resultado = numero % 3 and numero % 5

if resultado == 0:
    print ('FizzBuzz')

else:
    print (numero)
    
