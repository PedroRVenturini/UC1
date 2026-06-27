Nome = input("Nome: ")
Idade = int(input("Idade: "))
Nota1 = float(input("Nota1 "))
Nota2 = float(input("Nota2 "))
Nota3 = float(input("Nota3 "))

media = (Nota1 + Nota2 + Nota3)/3

if media>= 7.0:
   Situação = "Aprovado"
elif media>= 5.0:
   Situação = "Recuperação"
else:
   Situação = "Reprovado"

print(f'Nome: {Nome}')
print(f'Idade: {Idade}')
print(f'media: {media}')
print(f'Situação: {Situação}')