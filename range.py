# for i in range(1,11):
#     print(i)

exp = [2340,2500,2100,3100,2980]

total = 0

for i in range(len(exp)):
    print("Month: ",i+1,"Expense: ",exp[i])
    total = total + exp[i]

print("Total Expense" , total)