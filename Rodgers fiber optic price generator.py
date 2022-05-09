from ast import If


print("Welcome to Rodgers' fiber optic cable price generator.")
PROMPT = "What is your company's name? "
companyName = input(PROMPT)
print(f"\nWelcome, {companyName}!")
qtyNeeded = input("How many feet of fiber optic cable will you need today? ")
qtyNeeded = int(qtyNeeded)
if qtyNeeded < 100:
    totalPrice = qtyNeeded * 0.87
elif qtyNeeded >= 100 and qtyNeeded < 250:
    totalPrice = qtyNeeded * 0.80
elif qtyNeeded >= 250 and qtyNeeded < 500:
    totalPrice = qtyNeeded * 0.70
elif qtyNeeded >= 500:
    totalPrice = qtyNeeded * 0.50    
roundedTPrice = round(totalPrice,3)
print(f"\nYour total cost is ${roundedTPrice}")
print(f"\nThank you, {companyName} , for choosing Rodgers' fiber optic cable generator. Goodbye.")