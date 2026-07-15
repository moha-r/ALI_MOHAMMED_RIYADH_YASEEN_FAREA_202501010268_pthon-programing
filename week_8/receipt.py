def print_receipt(name, food, quantity, price, delivery_charges):

    subtotal = quantity * price
    service_charge = subtotal * 0.05
    grand_total = subtotal + service_charge + delivery_charges

    print("\n========== RECEIPT ==========")
    print(f"Customer Name : {name}")
    print(f"Food Item : {food}")
    print(f"Quantity : {quantity}")
    print(f"Price : RM {price:.2f}")
    print("----------------------------")
    print(f"Subtotal : RM {subtotal:.2f}")
    print(f"Service Charge (5%) : RM {service_charge:.2f}")
    print(f"Delivery Charges : RM {delivery_charges:.2f}")
    print("----------------------------")
    print(f"Grand Total : RM {grand_total:.2f}")
    print("============================")