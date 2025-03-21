dicti = {"China" : 143 , "India": 136 , "USA" : 32 , "Pakistan" : 21}
#
# command = input("What do yo want to do: ")
#
# if command == "print":
#     for d in dicti:
#         print(d , "==>" , dicti[d])
#
# elif command == "add":
#     add = input("Enter the name of the country: ")
#
#     if add not in dicti:
#         addval = input("Enter the population of the country: ")
#         dicti[add] = int(addval)
#         for d in dicti:
#             print(d, "==>", dicti[d])
#
#
# elif command == "remove":
#     remove = input("Enter the name of the country: ")
#
#     if remove in dicti:
#         del dicti[remove]
#         for d in dicti:
#             print(d, "==>", dicti[d])
#
# elif command == "query":
#     query = input("Enter the name of the country: ")
#
#     print(dicti[query])
#
# else:
#     print("Wrong Command")
#
#

#working for print

def printall():
    for name,population in dicti.items():
        print(name, "==>" , population)
    return

#addition

def add():
    newc = input("Enter the name of the country: ")

    if newc not in dicti:
        newcp = input("What is the population?: ")

        dicti[newc] = float(newcp)

        printall()

    return

#remove

def remove():
    remc = input("Enter the name of the country: ")

    if remc in dicti:
        del dicti[remc]
        printall()

    else:
        print("Country isn't in the list!")

    return

#query

def query():
    qc = input("Enter the name of the country: ")

    print(dicti[qc])

    return

operation = input("What do you want to do?: ")

operation = operation.lower()

if operation == "print":
    printall()

elif operation == "add":
    add()

elif operation == "remove":
    remove()

elif operation == "query":
    query()

else:
    print("Invalid Operation")



