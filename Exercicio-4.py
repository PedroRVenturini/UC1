temp = []

for i in range(6):
    Temperatura = float(input('Temperatura: '))
    temp.append(Temperatura)


for i in temp:
    if i <= 15:
        print('Frio')
    elif i >= 15 and i <= 28:
        print('Agradavel')
    else:
        print('Quente')        



