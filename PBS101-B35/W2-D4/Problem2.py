# Prompt the user to input the original price of the item
og_price = int(input("Enter the original price of the item: "))

# Check if the input price is non-negative
if og_price < 0:
    print("Invalid input, the price must be a non-negative number.")
else:
    # Check if the original price is greater than 20
    if og_price > 20:
        # Calculate the discounted price
        final_price = og_price * 0.9  # Applying a 10% discount
    else:
        # If the original price is 20 or less, no discount is applied
        final_price = og_price
    
    # Print the final price formatted as specified
    print("The final price of the item is: ",(final_price))
