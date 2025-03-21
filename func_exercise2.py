def triangle_area(type,base,height):
    if type == "triangle":
        area = (1/2) * int(base) * int(height)
    elif type == "rectangle":
        area = int(base) * int(height)
    else:
        area =  "invalid shape"
    return area

type = input("What is the shape type? ")
height = input("Enter the height: ")
base = input("Enter the height: ")

print("Area of the triangle is:" , triangle_area(type,base,height))
