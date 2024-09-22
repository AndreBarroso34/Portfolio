import os
import random

# Variáveis
num_bot = 0
num_ut = 0
soma = 0

# Função de gerar números
def generate_random_numbers():
    random_numbers = [random.randint(1, 10) for _ in range(3)]
    return random_numbers

num_bot = generate_random_numbers()

# Soma os números gerados para o computador
num_pc = sum(num_bot)

# Loop do jogo para o jogador pedir cartas
while input("Peça a carta apertando 's': ") == 's':
    pcartas = random.randint(1, 10)
    soma += pcartas
    print(f"Soma atual: {soma}")
    
    if soma > 21:
        print("Perdeste, o valor excedeu 21")
        break  # Sai do loop caso o jogador perca

# Resultado final do jogo
print("O computador teve: ", num_pc)
print("O jogador teve: ", soma)

# Verifica o resultado do jogo
if soma > 21:
    print("O pc ganhou, pois o jogador ultrapassou 21")
elif num_pc > 21 and soma > 21:
    print("Empataram, ambos ultrapassaram 21")
elif num_pc == soma:
    print("Empataram")
elif num_pc > 21:
    print("O jogador ganhou, o PC ultrapassou 21")
elif soma > num_pc:
    print("O jogador ganhou")
else:
    print("O pc ganhou")


    


