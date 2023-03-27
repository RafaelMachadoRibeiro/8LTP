lista = []
vm = 0

for i in range(50):
    num = float(input('Digite o '+str(i+1)+'º número: '))
    lista.insert(i,num)

vm = max(lista)
lm = lista.index(vm)

print('O maior número da lista é: ', vm)
print('A posição do maior número é: ', lm)