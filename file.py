f = open("E:\\data\\funny.txt","w")

f.write("I Love Data Science\n")
f.write("Cool!")
f.close()

f = open("E:\\data\\funny.txt","a")

f.write("Heh!")

f.close()

f = open("E:\\data\\funny.txt","r")
print(f.read())
f.close()

f = open("E:\\data\\funny.txt","r")
f_new = open("E:\\data\\funny_line_count.txt","w")
for line in f:
    tokens = line.split(' ')

    f_new.write("Word Count: "  + str((len(tokens))) + line )

f.close()
f_new.close()

with open("E:\\data\\funny.txt" , "r") as f:
    print(f.read())

print(f.closed)


