lista = []

for i in range(3):
    num = int(input('Digite o '+str(i+1)+'º elemento: '))
    lista.append(num)

n = int(input('Digite um número que você deseja descobrir a posição na lista: '))

if (n in lista):
    print(f'A posição {n} é {lista.index(n)}')
else:
    print("Não existe nenhum valor alocado a esta posição.")