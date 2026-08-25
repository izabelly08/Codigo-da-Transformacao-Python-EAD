'''


'''

import random
import math

def jogar():
    limite_inferior = 1
    limite_superior = 24

    numero_secreto = random.randint(limite_inferior, limite superior)



max_tentativas = 
math.ceil(math.log2(limite_superior - limite_inferior + 1))

print("===JOO DA ADIVINHACAO")
print(f"Tente adivinhar o numero entre {limite_inferior} e {limite_superior}.")
print(f"Voce tem {max_tentativas}tentativas!\n")

tentativas = 0
while tentativas < max_tentativas:
    palpite = int(input(f"Tentativa{tentativas + 1}: Digite seu palpite:"))
    tentativas += 1

    if palpite == numero-secreto:
        print(f"Parabens! Voce acertou em {tentativas} tentativas(s)!")
        break
     elif palpite < numero_secreto:
        print("O numero secreto é MAIOR.")
    else:
        print("O numero secretp é MENOR.")
else:
    print(f"\nFim de jogo! O numero era {numero_secreto}.")

    if_name_ == "_main_":
    jogar()
        
