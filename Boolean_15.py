while True:
    A = int(input('Enter A: '))
    B = int(input('Enter B: '))
    C = int(input('Enter C: '))

    print ((C>0 and B>0 and A<=0) or (C>0 and B<=0 and A>0) or (C<=0 and B>0 and A>0))
