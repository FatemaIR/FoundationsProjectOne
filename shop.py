####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "The Golden Cupcake"
signature_flavors = ["queen", "top", "lava", "dream", "magic"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print("Here is our Menu: ")
    for items in menu:
        print (items)
    print("\n")


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    print("Here are our original flavor cupcakes: ")
    for i in original_flavors:
        print(i)
    print("\n")


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    print("Here are our signature flavor cupcakes: ")
    for i in signature_flavors:
        print(i)
    print("\n")



def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if (order in menu or order in original_flavors or order in signature_flavors):
        return True
    else:
        return False 


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    order = input("Enter your order please: \n")
    while(order != "Exit"):
        if(is_valid_order(order)):
            order_list.append(order)
        order = input("Enter your order please: \n")
            
    else:
        return order_list



def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if (total >= 5):
        print("credit card payment is eligible.\n")
    else:
        print("credit card payment is NOT eligible.\n ...")




def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for item in order_list:
        if(item in menu):
            total = total + menu[item]
        elif (item in original_flavors):
            total = total + original_price
        else:
            total = total + signature_price

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for i in order_list:
        print(i)

    final_price = get_total_price(order_list)
    print("the total price:")
    print(final_price)

    card = accept_credit_card(final_price)
    print(card)

    print("******************")
    print(cupcake_shop_name)
    print("Thank you for shopping with us ^*^ ") 
    print("******************")


print_menu()
print_originals()
print_signatures()

last = get_order()
print_order(last)
