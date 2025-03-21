thing = "chair"

list1 = ["mouse" , "table" , "earbud" , "chair" , "graphics tab" , "pen"]

for i in list1:
    if i ==thing:
        print("Found!" , i)
        break
    else:
        print("Not found,",thing,"Let's try again!")