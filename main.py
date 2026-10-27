# main.py
# Simple Discount Calculator
# Note: This version intentionally contains a bug.

def final_price(price, discount_percent):
    # Bug: returns the original price without applying the discount
    return price


# Sample input
price = 200
discount_percent = 20

# Calculate and display the final price
result = final_price(price, discount_percent)

print("Original Price:", price)
print("Discount Percentage:", discount_percent, "%")
print("Final Price:", result)
