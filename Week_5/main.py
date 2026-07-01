from utils import calculate_total, print_receipt


customer_name = input("Customer name: ")

coffee_quantity = int(input("Coffee quantity: "))
tea_quantity = int(input("Tea quantity: "))
sandwich_quantity = int(input("Sandwich quantity: "))


if coffee_quantity < 0 or tea_quantity < 0 or sandwich_quantity < 0:
    print("Error: Quantities cannot be negative.")
else:
    total = calculate_total(
        coffee_quantity,
        tea_quantity,
        sandwich_quantity
    )

    print_receipt(
        customer_name,
        coffee_quantity,
        tea_quantity,
        sandwich_quantity,
        total
    )