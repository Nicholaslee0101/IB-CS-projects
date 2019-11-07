#Question 1
for i in range(10):
    for j in range(10):
        print('*', end=' ')
    print('')

#Question 2
for row in range(6):

    for column in range(6 - row):
        print(" ", end=" ")

    for column in range(1, row + 1):
        print("*", end=" ")

    for column in range(row - 1, 0, -1):
        print("*", end=" ")

    print("")