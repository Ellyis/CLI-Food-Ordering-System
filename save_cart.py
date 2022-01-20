import CHAI_LI_QI_TP061156_AND_YONG_KAI_BIN_TP061006 as Func

def save_cart(username, cart):
    old_cust = False  # Check either old customer or new customer
    with open(f"{username}.txt", "r+") as file:  # Open customer text file
        lines = file.readlines()  # Store menu contents into a variable
        file.seek(0)  # Place the file handler at the beginning of the file
        file.truncate()  # Set the file to certain byte. In this situation is delete all file contents
        for line in lines:
            if "cart" in line:
                old_cust = True
                break
        if old_cust is True:
            for line in lines:
                if "cart" in line:
                    new_cart = line.replace(line, cart + "\n")  # Replace old cart with final cart
                    file.write(new_cart)  # Write down the new cart
                else:  # If "cart" is not in line
                    file.write(line)  # Write back all the lines that are not related to cart
        else:  # If old_cust is False
            for line in lines:
                file.write(line)  # Write back all the lines that are not related to cart
            file.write("\n" + cart)  # Write down the final cart

save_cart("Bob", "cart;A1;A2;")



