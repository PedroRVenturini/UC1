"""produtos = []   
print('#' * 20, 'BEM VINDO A NARA HORTI FRUTI', '#' * 20)

while True:
    print("1 - Adicionar item")
    print("2 - Listar itens")
    print("3 - Sair")
    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        escolha_produto = input('Digite o produto que deseja ').title()
        produtos.append(escolha_produto)
    elif opcao == 2:
        if len(produtos) == 0:
            print('Nenhum produto cadastrado') 
        else:
            for i in produtos:
                print(f'Produto {i}')
    elif opcao == 3:
        break
    else:
        print('Escolha uma opção válida')"""

#Atividade final - UC1

alunos = []
print('#' * 20, 'BEM VINDO A NARA FIT', '#' * 20)

while True:
    print('1 - Cadastrar aluno')
    print('2 - Listar todos os alunos')
    print('3 - Ver estatisticas da academia')
    print('4 - Sair')
    opcao = int(input('Escolha uma opcao: '))

    if opcao == 1:
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        peso = float(input("Peso: "))
        altura = float(input("Altura: "))
        classificacao = imc

        imc = peso / (altura ** 2)

        if imc < 18.5:
            print('Abaixo do peso')

        elif imc <= 24.9:
            print('Peso normal') 

        elif imc <= 29.9:
            print('Sobrepeso')

        else:
            print('Obesidade')

        aluno = {
            'nome' : nome,
            'idade' : idade,
            'peso' : peso,
            'altura' : altura,
            'imc' : imc,
            "classificacao" : classificacao 
        }    
    alunos.append(aluno)

    print(f"Aluno {nome} cadastrado com sucesso")
    print(f'IMC: {imc: .2f} - {classificacao}')



