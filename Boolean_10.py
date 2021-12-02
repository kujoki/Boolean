while True:
    A = int(input('Enter A: '))
    B = int(input('Enter B: '))

    print ((A%2 == 0 and B%2 == 1) or (A%2 == 1 and B%2 == 0))
    # print((A+B)%2==1)
