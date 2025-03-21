d = {"Shakkhor" : 2110022 , "Sadik": 2110001 , "Fahmid" : 2110025}

# print(d["Sadik"])

print(d)

d["Arif"] = 2110045

print(d)

del d["Fahmid"]

print(d)

for name in d:
    print("name:" , name , "roll:" , d[name])

for roll,name in d.items():
    print("name:" , name , "role:", roll)

print("Arif" in d)
print(2110022 in d)

d.clear()

print(d)