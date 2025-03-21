#dictionary definition

Stocks = {"info" : [600,630,620] , "ril" : [1430, 1490 , 1567] , "mtl" : [234,180,160]}

#print

def printall():
    for stock,prices in Stocks.items():
        print(stock , "==>" , prices , round(sum(Stocks[stock]) / len(Stocks[stock]),2))

    return

def add():
    add_new = input("Stock to add: ")

    if add_new in Stocks:
        new_val = input("Enter new price: ")

        new_val = int(new_val)

        Stocks[add_new].append(new_val)

    else:
        new_val = input("Enter new price: ")

        new_val = int(new_val)

        Stocks[add_new] = [new_val]

    printall()

    return

operation = input("What do you want to do?: ")

if operation == "print":
    printall()

elif operation == "add":
    add()

