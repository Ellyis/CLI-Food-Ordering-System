import CHAI_LI_QI_TP061156_AND_YONG_KAI_BIN_TP061006 as Func

def update_cart(username, cart):
    separator = ";"
    if len(cart) > 0:  # Got food in cart
        codes = [code[0] for code in cart] # Extract all food codes from cart
        print(f"All food codes in cart: {codes}")
        code_in_file = ""
        for code in codes:
            code_in_file += f"{code}{separator}"  # Add all food codes
        final_cart = f"cart{separator}" + code_in_file
        print(f"Cart that need to be saved: {final_cart}")
        Func.save_cart(username, final_cart)
    else:  # No items in cart
        final_cart = f"cart{separator}"
        Func.save_cart(username, final_cart)

update_cart("Bob", [['A1',
                     'Black Pepper Chicken Burger',
                     '18.00',
                     'Chicken thigh grilled to perfection, coated with house-made black pepper sauce. Served with fries and salad.'],
                    ['A2',
                     'Spicy Grilled Chicken Burger',
                     '18.50',
                     'Grilled chicken thigh topped with special chili sauce. Served with fries and salad.']])
