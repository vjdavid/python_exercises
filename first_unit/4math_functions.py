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

square_root_one = math.sqrt(given_numbers[0])
square_toot_two = math.sqrt(given_numbers[1])
print("La raiz cuadrada de {} es {} y de {} es {}".format(given_numbers[0],
    square_root_one, given_numbers[1], square_toot_two))

