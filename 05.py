lista = []

for i in range(20):
    num = int(input('Digite o '+str(i+1)+'º número: '))
    lista.insert(i,num)
lista.reverse()

print(lista)