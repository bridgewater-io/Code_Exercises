print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
index = 1
weight = 185
planet = 7

planet_list = [
  ['Venus', 0.91],
  ['Mars', 0.38],
  ['Jupiter', 2.34],
  ['Saturn', 1.06],
  ['Uranus', 0.92],
  ['Neptune', 1.19]
]

# Write an if statement below:
for i in planet_list:
  if index == planet:
    weight = weight * i[-1]
    break
    index += 1
  else:
    print("Error")
    break
print(weight)
