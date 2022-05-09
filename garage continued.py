class Vehicle:
    def __init__(self):
        self.year = 0000
        self.make = "n/a"
        self.model = "n/a"
        self.rem_start = "n/a"

    def EnterData(self):
        self.year = int(input("What year is the vehicle?        :"))
        self.make = input    ("What is the make?                :")
        self.model = input   ("The Model?                       :")
        self.rem_start = input("Remote starter?                  :")
        print("")
        
    
    def print_vehicle(self):
        print(f"          Year:     {self.year}")
        print(f"          Make:     {self.make}")
        print(f"         Model:     {self.model}")
        print(f"Remote Starter:     {self.rem_start}")
        print("")

class Car(Vehicle):
    def EnterData(self):
        self.doors = input("How many doors is your car?      :")
        return super().EnterData()
            
    def print_vehicle(self):
        print("")
        print (f"Doors         :     {self.doors}")
        return super().print_vehicle()
        
class Truck(Vehicle):
    def EnterData(self):
        self.bed_length = input("How long is your bed length?      :")
        return super().EnterData()
            
    def print_vehicle(self):
        print("")
        print (f"Bed Length     :     {self.bed_length}")
        return super().print_vehicle()


garage = []
while True:
    choice = input("Would you like to enter a car (c), a truck (t), or quit (q)?  :")
    if choice == 'c':
        new_vehicle = Car()
        new_vehicle.EnterData()
        garage.append(new_vehicle)
    elif choice == 't':
        new_vehicle2 = Truck()
        new_vehicle2.EnterData()
        garage.append(new_vehicle2)
    elif choice =='q':
        print('\n'.join(map(str, garage))) 
        quit
    else:
        print("car, truck, or quit")

    go_on = input("Do you want to add another vehicle to the garage? ")
    if go_on.lower()[0] == 'y':
        continue
    else:
        print(garage)
        break
