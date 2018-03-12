#Victor David Jarillo Davila

given_number = int(input("Inserte un numero a multiplicar: "))

initializer = 1

while initializer < 21:
    product = initializer * given_number
    print("{} X {} = {}".format(initializer, given_number, product))
    initializer += 1
