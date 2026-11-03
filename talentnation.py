customer_name = " alice "
cleaned_name = customer_name.strip()
proper_name = cleaned_name.capitalize()
order = " espresso "
name = "Christopher"
customer = "Bob"
total = 12.0
raw_order_list = "latte,espresso,mocha"
menu_display = ""

items = raw_order_list.split(",")
menu_display = "\n".join(items)
new_order = "espresso with milk and caramel and chocolate"

def order_drink(drink, size):
    print("Dispensing " + size + " " + drink)


cups_ordered = 3
price_per_cup = 4.50
customer_receipt = ""

def calculate_price(count, cost):
    total = count * cost
    return total

customer_receipt = calculate_price(cups_ordered, price_per_cup)

def add_tax(subtotal):
    return subtotal * 1.08

final_total = add_tax(10.0)

def make_custom_drink(base_drink, milk_type, sugar_packets):
    description = f"{base_drink} with {milk_type} milk"

    if sugar_packets > 0:
        description = description + f" and {sugar_packets} sugar packets"

    return description

order1 = make_custom_drink("Latte", "almond", 2)
order2 = make_custom_drink("Cappuccino", "whole", 0)

def test_scope():
    secret_recipe = "Vanilla Syrup"
    print(secret_recipe)


shop_name = "Espresso Cart"
def print_shop():
    print("Welcome to " + shop_name)


count = 0

def increment():
    global count
    count = count + 1
    print(count)

increment()
increment()

def run_coffee_cart():
    current_order = "Espresso"

    def change_order(new_drink):
        nonlocal current_order
        current_order = new_drink
        print(f"Order updated to: {current_order}")

    change_order("Latte")
    print(f"Final cart order: {current_order}")

run_coffee_cart()

def outer():
    x = "original"
    def inner():
        nonlocal x
        x = "modified"
    inner()
    print(x)
outer()

print_shop()
test_scope()
print(order1)
print(order2)
print(final_total)
print(customer_receipt)
order_drink("espresso", "large")
print(new_order.split("with", maxsplit=1))
print(items)
print(menu_display)
print(f"Thank you, {customer}! Total: N{total:.2f}")
print(name[0:5])
print(order.strip().upper())
print("[" + proper_name +"]")