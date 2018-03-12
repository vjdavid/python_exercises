#Victor David Jarillo Davila

def highest_number(a, b):
    if a > b:
        return a
    else:
        return b

def highest_of_tree(a, b, c):
    return highest_number(a, highest_number(a, b))

def main():
    a = int(input("Inserte el valor de A: "))
    b = int(input("Inserte el valor de B: "))
    c = int(input("Inserte el valor de C: "))

    highest = highest_of_tree(a, b, c)

    print("El valor mayor es {}".format(highest))


main()
