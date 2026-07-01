# Prices of the café items
COFFEE_PRICE = 8.50
TEA_PRICE = 6.00
SANDWICH_PRICE = 12.00


# Function for calculating the total bill
def calculate_total(coffee, tea, sandwich):
    coffee_cost = coffee * COFFEE_PRICE
    tea_cost = tea * TEA_PRICE
    sandwich_cost = sandwich * SANDWICH_PRICE
    total = coffee_cost + tea_cost + sandwich_cost

    return total


# Function for printing the receipt
def print_receipt(customer_name, coffee, tea, sandwich, total):
    print("\n===== RECEIPT =====")
    print(f"Customer : {customer_name}")
    print(f"Coffee   : {coffee}")
    print(f"Tea      : {tea}")
    print(f"Sandwich : {sandwich}")
    print(f"Total = RM {total:.2f}")