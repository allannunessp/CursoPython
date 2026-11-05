import math

an = float(input("Digite o ângulo que deseja: "))

s = math.sin(math.radians(an))
c = math.cos(math.radians(an))
t = math.tan(math.radians(an))

print("O ângulo de {} tem o Seno de {:.2f} ".format(an, s))
print("O ângulo de {} tem o Cosenp de {:.2f} ".format(an, c))
print("O ângulo de {} tem o Tangente de {:.2f} ".format(an, t))
