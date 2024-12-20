# Desafio de projeto #2 - classificador de rank com base em vitórias e derrotas

# dê um nome ao seu herói
heroName = input("Dê um nome ao seu herói: ")

# função de calculo
def calculateRank(victories, loses):
    rank = victories - loses
    return rank

# caixa de ranks 
ranks = ["Ferro", "Bronze", "Prata", "Ouro", "Diamante", "Lendário", "Imortal"]

# retorno da função
victoryBalance = calculateRank(int(input("Digite o n° de vitórias: ")), int(input("Digite o n° de derrotas: ")))

# resultado de rank
if victoryBalance <= 10:
    print(f"O herói tem o saldo de {victoryBalance} vitórias e está no nível de {ranks[0]}")

elif victoryBalance > 10 and victoryBalance < 21:
    print(f"O herói tem o saldo de {victoryBalance} vitórias e está no nível de {ranks[1]}")

elif victoryBalance > 20 and victoryBalance < 51:
    print(f"O herói tem o saldo de {victoryBalance} vitórias e está no nível de {ranks[2]}")

elif victoryBalance > 50 and victoryBalance < 81:
    print(f"O herói tem o saldo de {victoryBalance} vitórias e está no nível de {ranks[3]}")

elif victoryBalance > 80 and victoryBalance < 91:
    print(f"O herói tem o saldo de {victoryBalance} vitórias e está no nível de {ranks[4]}")

elif victoryBalance > 90 and victoryBalance < 101:
    print(f"O herói tem o saldo de {victoryBalance} vitórias e está no nível de {ranks[5]}")

else: 
    print(f"O herói tem o saldo de {victoryBalance} vitórias e está no nível de {ranks[6]}! esse é o rank mais alto!")

# mensagem final
print(f"Continue se esfoçando {heroName}!")