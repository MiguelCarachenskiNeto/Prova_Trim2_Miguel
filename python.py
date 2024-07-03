import os
from datetime import datetime

estacoes = ["Outono", "Inverno", "Primavera", "Verão"]

os.system("cls")

data = input('Insira uma data em formato dd/mm: ')

try:
    dia, mes = map(int, data.split('/'))
    input_date = datetime(year=2024, month=mes, day=dia)

    if (3, 20) <= (mes, dia) <= (6, 20):
        i = 0

    elif (6, 21) <= (mes, dia) <= (9, 22):
        i = 1
        
    elif (9, 23) <= (mes, dia) <= (12, 21):
        i = 2

    else:
        i = 3
        
    print(f"\nA estação na data {dia}/{mes} será: {estacoes[i]}\n")

except ValueError:
    print("Data inválida")
