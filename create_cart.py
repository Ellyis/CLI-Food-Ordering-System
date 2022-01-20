import CHAI_LI_QI_TP061156_AND_YONG_KAI_BIN_TP061006 as Func

def create_cart(username):
    cart = []
    with open(f"{username}.txt", "r") as file:  # Open customer text file
        lines = file.readlines()  # Store each line into a list
        for line in lines:
            if "cart" in line:
                print(f"Line before strip and split: {line}")
                code = line.strip("\n").split(";")  # Split food codes into a list
                print(f"Line after strip and split: {code}")
                code.pop()  # Remove the last element from the list which is an empty string
                print(f"List after pop: {code}")
                for i in range(len(code) - 1):  # Loop through the length of code
                    food = Func.food_match(code[i + 1])  # Obtain each food code
                    cart.append(food)  # Add into cart
                print(f"The saved cart: {cart}")
                break
    return cart
create_cart("Jam")