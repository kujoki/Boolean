while True:
    A = int(input('Enter A: '))
    B = int(input('Enter B: '))
    C = int(input('Enter C: '))

    print (A==(-B) or B==(-C) or A==(-B) or (A==(-B) and B==(-C) and A==(-B)))
