size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
    for length in range(size):
        print("*", end="")
    row += 1
    print("")