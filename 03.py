somnt = 0
mednt = 0
tamnt = 0
contAc = 0
contAb = 0
lista_nota = []
lista_matr = []

for i in range(50):
    nota = int(input("Digite a nota do "+str(i+1)+"º aluno: "))
    lista_nota.insert(i,nota)
    matr = int(input("Digite a matricula do "+str(i+1)+"º aluno: "))
    lista_matr.insert(i,matr)

somnt = sum(lista_nota)
tamnt = len(lista_nota)
mednt = somnt / tamnt

for j in range(len(lista_nota)):
    if (lista_nota[j]>mednt):
        contAc += 1
    elif (lista_nota[j]<mednt):
        contAb += 1

print(f'A média dos alunos é: {mednt:,.2f}')
print('A quantidade de alunos acima da média é: ',contAc)
print('A quantidade de alunos abaixo da média é: ',contAb)