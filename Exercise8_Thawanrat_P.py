usernameInput = input("Username: ")
passwordInput = input("Password: ")
if usernameInput == "customer" and passwordInput == "0000":
    print(">> Done, Welcome !")

    print("------ Welcome to my Shop ------")
    print(">> Select item you want to buy !")
    print("1. iPhone        35,000 THB")
    print("2. Macbook       56,000 THB")
    print("3. iPad          25,900 THB")
    print("4. AppleWatch     9,900 THB")
    userSelected = int(input("Select an option: "))

    prices = {
        1: 35000,
        2: 56000,
        3: 25900,
        4: 9900
    }

    if userSelected in prices:
        quantity = int(input("Quantity to be purchased:"))
        totalQuantity = prices[userSelected] * quantity
        vat = 7 / 100
        totalVat = totalQuantity * vat
        totalPrice = (totalQuantity * vat) + totalQuantity

        print("-------------------------")
        print("Vat 7%:", totalVat)
        print("Your total price is:", totalPrice, "THB")
    else:
        print("Invalid option")
else:
    print(">> Invalid username or password")
print("-------------------------")
print(":) Thank you !")
