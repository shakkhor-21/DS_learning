def circle(radius):
    area = round(3.14159 * radius ** 2,2)
    circumference = round(2 * 3.14159 * radius,2)
    diameter = round(2 * radius,2)

    print("The area , circumference and diameter are: " , area, circumference , diameter)

    return

radius = float(input("Enter the radius: "))

circle(radius)
