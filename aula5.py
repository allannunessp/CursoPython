import math

num = int(input(" Digite um número: "))

raiz = math.sqrt(num)

print(" A raiz de {} é igual a {} ".format(num, raiz))


# Desafio 16

n = float(input(" Digite um número: "))
i = math.trunc(n)
print(" Seu número inteiro é {} ".format(i))

# Desafio 17

a = float(input(" Digite um número: "))
b = float(input(" Digite outro número: "))
ap = math.pow(a, 2)
bp = math.pow(b, 2)
h = ap + bp
hf = math.sqrt(h)
print(" A hipotenusa é de {} ".format(hf))

# Desafio 18

# Desafio 19

import random

print(random.choice(["Maria", "Lucas", "Fabio", "Pedro"]))

# Desafio 20

lista_nome = ["Maria", "Lucas", "Fabio", "Pedro"]
print(random.sample(lista_nome, 4))
