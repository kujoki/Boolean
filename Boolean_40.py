while True:
    x_1 = int(input('Введите координату коня x_1: '))
    y_1 = int(input('Введите координату коня y_1: '))
    x_2 = int(input('Введите координату коня x_2: '))
    y_2 = int(input('введите коодинату коня y_2: '))

    print ((abs(x_1-x_2)==1 and abs(y_1-y_2)==2) or (abs(x_1-x_2)==2 or abs(y_1-y_2)==1))
