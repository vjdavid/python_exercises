#Victor David Jarillo Davila

list = [2, 'Mangos', 3, 0.49, 5, 0.0000123, 'manzanas', 113.52342324, 0.54,
        'melones']

size = 0
while size < 10:
    print("El tipo de dato del elemento [{}] {} es: {}".format(size, list[size], type(list[size])))
    size += 1
