from food_order import calculate_total


def test_order1():
    assert calculate_total(10, 2) == 20


def test_other_valid_orders():
    # Test if total food order is equal to 30
    assert calculate_total(10, 3) == 30

    # Test if total food order is equal to 100
    assert calculate_total(20, 5) == 100

    # Test if total food order is equal to 10
    assert calculate_total(5, 2) == 10


def test_invalid_price():
    # Test if total food order is equal to "invalid price"
    assert calculate_total(0, 2) == "invalid price"
    assert calculate_total(-10, 2) == "invalid price"


def test_invalid_quantity():
    # Test if total food order is equal to "invalid quantity"
    assert calculate_total(10, 0) == "invalid quantity"
    assert calculate_total(10, -2) == "invalid quantity"
