price = int(input("Enter price: "))

def vatCalculate(price):
    result = price * 7 // 100 + (price)
    return result

print("Total Price =", vatCalculate(price))
