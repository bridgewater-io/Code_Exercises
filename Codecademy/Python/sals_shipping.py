# Change the weight variable below to see different prices per shipping weight
weight = 4.8

# DO NOT CHANGE BELOW #
cost = 0

# Ground shipping
flat_charge = 20

if weight <= 2:
  cost = weight * 1.50
elif weight <= 6:
  cost = weight * 3.00
elif weight <= 10:
  cost = weight * 4.00
else:
  cost = weight * 4.75

cost += flat_charge

print(f"Ground Shipping: ${cost:.2f}")

# Ground Shipping Premium
ground_shipping_premium = 125.00

print(f"Ground Shipping Premium: ${ground_shipping_premium:.2f}")

# Drone Shipping
if weight <= 2:
  cost = weight * 4.50
elif weight <= 6:
  cost = weight * 9.00
elif weight <= 10:
  cost = weight * 12.00
else:
  cost = weight * 14.25

print(f"Drone Shipping: ${cost:.2f}")



