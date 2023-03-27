lista = []
soma = 0

for i in range(12):
    num = float(input('Digite o '+str(i+1)+'º número: '))
    lista.insert(i,num)

x = int(input('Digite a posição X (entre 0 e 11): '))
y = int(input('Digite a posição Y (entre 0 e 11): '))

soma = lista[x] + lista[y]

print('A soma dos valores é igual a: ', soma)