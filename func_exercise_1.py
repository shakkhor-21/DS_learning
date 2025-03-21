def triangle_area(base,height):
    area = (1/2) * int(base) * int(height)
    return area

height = input("Enter the height: ")
base = input("Enter the height: ")

print("Area of the triangle is:" , triangle_area(base,height))
