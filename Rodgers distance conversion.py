def miles_km():
    miles = input("\nHow many miles are you converting?")
    try:
        miles = float(miles)
        km = miles * 1.60934
        print(f"\n{miles} miles is {km} kilometers. ")
    except ValueError:
        print("That was not a number!")
def km_miles():
    km = input("\nHow many kilometers are you converting?")
    try:
        km = float(km)
        miles = km*0.621371
        print(f"\n{km} kilometers is {miles} miles.")
    except ValueError:
        print("That was not a number!")

miles = 0
km = 0
choice = ""
while choice != "q" or choice != "Q":
    choice = input("Would you like to convert miles to Kilometers (m), kilometers to miles (k) or q to quit?")
    try:
        if choice == "m" or choice == "M":
            miles_km()
        elif choice == 'k' or choice == 'K':
            km_miles()
        elif choice == 'q' or choice == "Q":
            break
        else:
            print("\nI'm sorry what was that choice?")
    except NameError:
        print("\nI'm sorry. What was that choice?")       