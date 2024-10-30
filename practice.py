# Create a function named calculate_discount(price, discount_percent) that calculates the final price after 
# applying a discount. The function should take the original price (price) and the discount percentage 
# (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
def calculate_discount(price , percentage_discount):
    if percentage_discount >= 20:
        discount = price * (percentage_discount / 100)
        net_price = price - discount
        return net_price
    else: 
        return price
    
print(calculate_discount(500, 30))
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage.
#  Print the final price after applying the discount, or if no discount was applied, print the original price
price = 0
percentage_discount = 0
price = int(input("enter the original price of the product: "))
percentage_discount = int(input("enter the discount given on the product: "))

print(calculate_discount(price, percentage_discount ))