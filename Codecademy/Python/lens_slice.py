# Your code below:

# Step 1: List containing all the types of toppings for the pizza
toppings = [
  "pepperoni",
  "pineapple",
  "cheese",
  "sausage",
  "olives",
  "anchovies",
  "mushrooms"
]

# Step 2: List containing the prices of pizzas in order by topping
prices = [
  2,
  6,
  1,
  3,
  2,
  7,
  2
]

# Step 3: Counting occurrences of how many pizzas cost $2 and storing in a variable and displaying it
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Step 4: Finding the total number of elements in the toppings list and storing it in a variable
num_pizzas = len(toppings)

# Step 5: Outputting information about our pizzas
print(f"We sell {num_pizzas} different kinds of pizza!")

# Step 6: Creating a 2D list to represent the type of pizza and its price
pizza_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
]

# Step 7: Outputting our pizza to prices information
print(pizza_and_prices)

# Step 8: Sorting our pizza prices in ascending order
pizza_and_prices.sort() # Could also do a sort() function with a new list if we need this data preserved

#Step 9: Storing the first element in a variable to represent the cheapest pizza
cheapest_pizza = pizza_and_prices[0]

# Step 10: Storing the last element to represent the most expensive slice
priciest_pizza = pizza_and_prices[-1]

# Step 11: Removing pizza out of stock, since we want the last removed, pop() will remove the last element by default without an parameter needed
pizza_and_prices.pop()

# Step 12: Adding a new pizza slice to replace 'anchovies' and resorting to maintain the proper order
pizza_and_prices.append([2.5, "peppers"])
pizza_and_prices.sort()

# Step 13: Storing the three cheapest pizzas in a new variable
three_cheapest = pizza_and_prices[:3]

# Final step: displaying the 3 cheapest pizzas
print(three_cheapest)

# Bonus: Displaying the modified pizza_and_prices list
print(f"\nHere are our updated items and prices: {pizza_and_prices}")

