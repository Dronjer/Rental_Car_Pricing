# This is car rental service program using python. Object Oriented Programming
import sys

class Rental:

    def __init__(self, list_of_cars):
        self.cars = list_of_cars

    def display_models(self):
        for cars in self.cars:
            print(cars)

    def suv_pricing(self, SUV):
        self.SUV = int(input('Enter the number of hours you want to borrow the cars: '))
        Price = self.SUV*100
        print('Your total in US dollars is :', Price)

    def sports_pricing(self, Sport):
        self.Sport = int(input('Enter the number of hours you want to borrow the cars: '))
        Price = self.Sport*200
        print('Your total in US dollars is :', Price)

    def sedan_pricing(self, Sedan):
        self.Sedan = int(input('Enter the number of hours you want to borrow the cars: '))
        Price = self.Sedan*80
        print('Your total in US dollars is :', Price)

    def hatchback_pricing(self, Hatchback):
        self.Hatchback = int(input('Enter the number of hours you want to borrow the cars: '))
        Price = self.Hatchback*40
        print('Your total in US dollars is :', Price)

class Customer:

    def request_suv(self):
        print('The price for the SUV is $100/hr')

    def request_sport(self):
        print('The price of the Sports Vehicle is $200/hr')

    def request_sedan(self):
        print('The price of the sedan vehicle is $80/hr')

    def request_hatchback(self):
        print('The price of the hatch back is $40/hr')

def main():
    borrow = Rental(['SUV', 'Sport', 'Sedan', 'Hatchback'])
    guest = Customer()

    l = True

    while l == True:
        print("""---- This is the menu for the car rental service ----
              1. Display all the available cars
              2. The pricing for the SUV
              3. The pricing for the Sports
              4. The pricing for the Sedan
              5. The pricing for the Hatchback
              6. Exit """)

        option = int(input('Enter the option :'))

        if option == 1:
            borrow.display_models()
        elif option == 2:
            borrow.suv_pricing(guest.request_suv())
        elif option == 3:
            borrow.sports_pricing(guest.request_sport())
        elif option == 4:
            borrow.sedan_pricing(guest.request_sedan())
        elif option == 5:
            borrow.hatchback_pricing(guest.request_hatchback())
        else:
            sys.exit()

main()
