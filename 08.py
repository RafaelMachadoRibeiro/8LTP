lista = []
soma = 0
med = 0
s13 = 0
stt = 0

for i in range (30):
    ida = int(input('Digite a idade do '+str(i+1)+'º aluno: '))
    lista.insert(i,ida)

soma = sum(lista)
med = soma/len(lista)

for j in range(len(lista)):
    if(lista[j]>13):
        s13 = s13 + 1
        if(lista[j]>med):
            stt = stt + 1

print('A quantidade de alunos maiores que 13 anos são: ', s13)
print('A quantidade de alunos maiores que a média são: ', stt)
    