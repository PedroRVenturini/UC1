'''temp = []

for i in range(6):
    Temperatura = float(input('Temperatura: '))
    temp.append(Temperatura)


for i in temp:
    if i <= 15:
        print('Frio')
    elif i >= 15 and i <= 28:
        print('Agradavel')
    else:
        print('Quente')'''       


def calcular_imc(peso, altura):
    imc =  peso / (altura**2) 
    return imc

def tratamento_altura(mensagem):
    while True:
        try:
            altura = int(input(mensagem))
            print('Altura cadastrada')
            break
        except ValueError:
            print('Digite apenas os Nº sem pontos')
    return altura

def tratamento_peso():
    while True:
        try:
            peso = float(input('Qual o seu peso? '))
            print('Peso cadastrado')
            break
        except ValueError:
            print('Digite apenas Nº válidos')
    return peso


alunos = {'nome' : [],
          'altura': [],
          'peso': [],
          'imc' : []}


while True:
    nome = input('Qual seu nome? ')
    altura = tratamento_altura('Qual a sua altura')
    peso = tratamento_peso()
    imc = calcular_imc(peso, altura)

    alunos['nome'].append(nome)
    alunos['altura'].append(altura)
    alunos['peso'].append(peso)
    alunos['imc'].append(imc)
    break

for i in range(len(alunos['nome'])):
    print(f'{alunos["nome"][i]}, seu imc é de {round(alunos['imc'][i]*100,2)} %')
