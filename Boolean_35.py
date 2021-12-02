x_1 = int(input('Enter x_1: '))
y_1 = int(input('Enter y_1: '))
x_2 = int(input('Enter x_2: '))
y_2 = int(input('Enter y_2: '))

print ((x_1%2 == 0 and y_1%2 == 0 and x_2%2 == 0 and y_2%2 == 0) or (x_1%2 == 1 and y_1%2 == 1 and x_2%2 == 1 and y_2%2 == 1) or (x_1%2 ==1 and y_1%2 == 0 and x_2%2 == 0 and y_2%2 == 1) or (x_1%2 == 0 and y_1%2 == 1 and x_2%2 == 1 and y_2%2 == 0))
