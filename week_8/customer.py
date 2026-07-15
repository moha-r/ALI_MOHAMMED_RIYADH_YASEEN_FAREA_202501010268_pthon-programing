def get_customer():

    print("=== Customer Information ===")
    name = input("Enter the name: ")
    food = input("Cake/Muffin:")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price of the food item: "))
    delivery_charges = input("delivery charges (Y/N): ")

    if delivery_charges == "Y":
        delivery_charges = 5.00
    else:
        delivery_charges = 0.00

    return name, food, quantity, price, delivery_charges