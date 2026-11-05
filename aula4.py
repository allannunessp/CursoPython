n1 = int(input("Digite um número: "))
print(" O número anterior é {} , e o numero seguinte é {} ".format(n1 - 1, n1 + 1))


n1 = int(input("Digite um número: "))
print(
    " Seu dobro é {} , seu triplo é {} e sua raiz quadrada é {:.2f} ".format(
        n1 * 2, n1 * 3, n1 ** (1 / 2)
    )
)
# Programa de notas

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

print("A média entre {} e {} é igual a {}".format(n1, n2, (n1 + n2) / 2))

# conversão de medidas

m = float(input("Digite uma distância em metros: "))
print(
    "A distância de {} metros corresponde a {} centímetros e {} milímetros".format(
        m, m * 100, m * 1000
    )
)

# proximo exercício

n1 = int(input("Digite um número: "))

print(" A tabuada de {} é: ".format(n1))
print("{} x 1 = {} ".format(n1, n1 * 1))
print("{} x 2 = {} ".format(n1, n1 * 2))
print("{} x 3 = {} ".format(n1, n1 * 3))
print("{} x 4 = {} ".format(n1, n1 * 4))
print("{} x 5 = {} ".format(n1, n1 * 5))
print("{} x 6 = {} ".format(n1, n1 * 6))
print("{} x 7 = {} ".format(n1, n1 * 7))
print("{} x 8 = {} ".format(n1, n1 * 8))
print("{} x 9 = {} ".format(n1, n1 * 9))
print("{} x 10 = {} ".format(n1, n1 * 10))


# proximo exercício

n1 = float(input("Digite o valor em R$:    "))
print("O valor de R$ {} corresponde a US$ {:.2f} ".format(n1, n1 / 3.27))

# proximo exercícioq

l1 = float(input("Digite a largura da parede: "))
h1 = float(input("Digite a altura da parede: "))
area = l1 * h1
litros = area / 2  # 1 litro a cada 2 metros quadrados
print(
    "A área da parede é {} m² e serão necessários {} litros de tinta para pintá-la.".format(
        area, litros
    )
)

# proximo exercício

p1 = float(input("Digite o preço do produto: "))
print(
    "O produto que custa R$ {} com 5% de desconto sai por R$ {:.2f} ".format(
        p1, p1 * 0.95
    )
)

# proximo exercício

s1 = float(input("Digite o salário do funcionário: "))
print(
    "O funcionário que ganha R$ {} com 15% de aumento passará a ganhar R$ {:.2f} ".format(
        s1, s1 * 1.15
    )
)

# proximo exercício

c = float(input("Digite a temperatura "))
f = ((c * 9) / 5) + 32

print(" A temperatura de {} C em graus F é de {}".format(c, f))


# Aluguel de carro

dia = int(input("Quantos dias o carro foi alugado? "))
km = float(input("Quantos km o carro percorreu? "))
print(
    " O valor de {} dias alugado é de R${} \n "
    " E o valor de {} Km rodados é de R${} \n"
    " Para um total de R${}".format(dia, dia * 60, km, km * 0.15, dia * 60 + km * 0.15)
)
