# main.py
# Simple Discount Calculator
# Note: This version intentionally contains a bug.
def final_price(price, discount_percent):
    discount = price * discount_percent / 100
    return price - discount

print(final_price(200, 20))  # Expected output: 160.0


# Sample input
price = 200
discount_percent = 20

# Calculate and display the final price
result = final_price(price, discount_percent)

print("Original Price:", price)
print("Discount Percentage:", discount_percent, "%")
print("Final Price:", result)
