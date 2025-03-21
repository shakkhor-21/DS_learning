def star_pattern(row):
    r = 1
    for r in range(int(row)+1):
        i = 0
        for i in range(r):
            print("*" , end="")
        print()

# row = input("Enter row number: ")

star_pattern(3)
