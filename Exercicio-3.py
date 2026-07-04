'''for i in range(5):
    print(i)

for i in range(1,6):
    print(i)    
    
for i in range(1,11):
    print(i)

for i in range(0,10,2):
    print(i)

for i in range(5, 0, -1):
    print(i)

for i in range(100, 0, -5):
    print(i)'''

'''while True:
    idade = int(input("Digite sua idade: "))
    if idade >= 0:
        break
    print("Idade invalidade! Tente novamente")

print(f'Idade Registrada: {idade}')'''

'''contador = 1
while contador <= 5:
    print(f'Contagem: {contador}')
    contador += 1
print('Fim!')'''

'''frutas = ['maca', 'banana', 'uva', 'pera'] #lista de strings
notas = [8.5, 7.0, 8.0, 9.0]
vazia = []

print(frutas)
frutas.append('manga')
print(frutas)'''

'''nome = ['goku', 'naruto']
for i in nome:
    print(i)

for i in range(len(nome)): 
    print(f"{i}: {nome[i]}")'''

'''for i in range(1,6):
    n = float(input(f"Numero {i}: "))
    print(f"dobro: {n*2}\n triplo: {n*3}\n quadruplo: {n*4}")'''

'''nomes = ['Ana', 'João', 'Pedro', 'Anderson', 'Renato']
for i in nomes:
    print(f'Bem-vindo(a), {i}!')'''

'''for i in range(10):
    Nome = input("Nome: ")
    Nota1 = float(input("Nota1 "))
    Nota2 = float(input("Nota2 "))
    media = (Nota1 + Nota2) / 2

    if media >= 7.0:
       print(f'O(a) Aluno(a teve a nota media de {media} e ficou aprovado)')
    elif media>= 5.0:
       print(f'O(a) Aluno(a teve a nota media de {media} e ficou recuperação)')
    else:
       print(f'O(a) Aluno(a teve a nota media de {media} e ficou reprovado)')'''

'''nome = ['goku', 'naruto']
idade = [55, 17]
for i in range(len(nome)):
    print(f'O {nome[i]} tem {idade[i]} anos')'''
nome = []
idade = []
estado = []

for i in range(3):
    candidato = input('Nome: ')
    estado_candidato = input('Estado: ')
    idade_candidato = int(input('Idade: '))

    if idade_candidato >= 18:
        nome.append(candidato)
        estado.append(estado_candidato)
        idade.append(idade_candidato)

    else:
        print('A vaga é apenas para candidato maiores de 18 anos')

for i in range(len(nome)):
    print(f'O candidato {nome[i]} esta cadastrado')
