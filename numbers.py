#Victor David Jarillo Davila

default_value = True

for number in range(1, 51):
    if default_value:
        print("Interno: {}".format(number))
        default_value = False
    else:
        print("\tExterno: {}".format(number))
        default_value = True
