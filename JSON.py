book = {}

book['Hasnat'] = {
    'name' : 'Hasnat' ,
    'address' : 'Dhaka, Bangladesh',
    'phone' : 23556
}

book['Sadiq'] = {
    'name' : 'Sadik' ,
    'address' : 'Lalmonirhadt, Bangladesh',
    'phone' : 23176
}

import json

s = json.dumps(book , indent = 4)

print(s)

with open("d://book.txt","w") as f:
    f.write(s)