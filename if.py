indian = ["samosa" , "daal" , "naan"]
chinese = ["egg role" , "pot sticker" , "fried rice"]
italian = ["pizza" , "pasta" , "risotto"]

dish = input("Enter a dish name")

if dish in indian:
    print("Indian")
elif dish in chinese:
    print("Chinese")
else:
    print("Italian")