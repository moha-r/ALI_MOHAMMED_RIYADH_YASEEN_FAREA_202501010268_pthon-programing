def calculate_total(price, quantity):
    """Calculate the total price of a food order.

    Returns an error message when the price or quantity is invalid.
    """
    if (
        isinstance(price, bool)
        or not isinstance(price, (int, float))
        or price <= 0
    ):
        return "invalid price"

    if (
        isinstance(quantity, bool)
        or not isinstance(quantity, int)
        or quantity <= 0
    ):
        return "invalid quantity"

    return price * quantity
