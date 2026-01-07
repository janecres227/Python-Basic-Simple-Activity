product_name = "Wireless Mouse"
price = 29.99
quantity = 5
discount_percentage = 10

#Calculations
sub_total = price * quantity
discounted = sub_total * discount_percentage / 100
final_total = sub_total - discounted

#Displaying the receipt
print(f"Product name: {product_name}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {sub_total}")
print(f"Discount: {discounted}")
print(f"Final Total: {final_total}")
