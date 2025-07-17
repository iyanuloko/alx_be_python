square_size = int(input("Enter the size of the pattern: "))
row_count = square_size
while row_count > 0:
    for _ in range(square_size):
        print("*", end="")
    print()
    row_count -= 1
