while True:
    A = int(input('Enter A: '))

    m = A//100
    k = (A//10)%10
    r = A - (100*m + 10*k)

    print (m<k<r)
