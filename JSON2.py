import json

f = open("d://book.txt")
s = f.read()

print(s)

book = json.loads(s)

print(book)

print(type(s))
print(type(book))

print(book['Sadik']['name'])

# for title,entries in book.items():
#     print(title,entries)

for person in book:
    print(book[person])


