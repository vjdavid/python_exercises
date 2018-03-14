#Victor David Jarillo Davila

import math

initializer = 1
given_numbers = []

while initializer < 3: 
     given_numbers.append(int(input("Por favor inserta 2 numeros: ")))
     initializer += 1

print("sqrt de {} y {}".format(given_numbers[0], given_numbers[1]))
print("pow de {} y {}".format(given_numbers[0], given_numbers[1]))
print("cos de {} y {}".format(given_numbers[0], given_numbers[1]))
print("sin de {} y {}".format(given_numbers[0], given_numbers[1]))
print("tan de {} y {}".format(given_numbers[0], given_numbers[1]))

print("Valores originales: A = {}, B = {}".format(given_numbers[0],
    given_numbers[1]))

c = math.sqrt(given_numbers[0])
d = math.sqrt(given_numbers[1])
print("La raiz cuadrada de {} es {} y de {} es {}".format(given_numbers[0], c, given_numbers[1], d))

e = math.pow(given_numbers[0], 2)
f = math.pow(given_numbers[1], 2)
print("La potencia de {} es {} y de {} es {}".format(given_numbers[0], e, given_numbers[1], f))

g = math.cos(given_numbers[0])
h = math.cos(given_numbers[1])
print("El coseno de {} es {} y de {} es {}".format(given_numbers[0], g, given_numbers[1], h))

h = math.sin(given_numbers[0])
i = math.sin(given_numbers[1])
print("El seno de {} es {} y de {} es {}".format(given_numbers[0], h, given_numbers[1], i))

j = math.tan(given_numbers[0])
k = math.tan(given_numbers[1])
print("La tangente de {} es {} y de {} es {}".format(given_numbers[0], j, given_numbers[1], k))
