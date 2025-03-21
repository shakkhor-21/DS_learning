def calculate_total(exp):
   total = 0
   for item in exp:
       total = total + item
   return total

tom = [322,284,307,363]
joe = [223,482,703,363]

tom_total = calculate_total(tom)
joe_total = calculate_total(joe)

print("Tom's Total Cost: ",tom_total)
print("Joe's Total Cost: ",joe_total)


