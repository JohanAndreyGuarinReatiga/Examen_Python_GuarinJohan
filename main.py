from menu.calculateTax import designCalculateTax
from menu.seeList import desginSeeList
from time import sleep
import os
import keyboard

while True:
    print("""
    ---------------------------------------------------
                    TAXES CALCULATOR
    ---------------------------------------------------""")
    print("""
    Choose an option:
    1. Calculate taxes in a product or a service
    2. See the list of types of taxes
    3. Leave
    ---------------------------------------------------
    """)
    option = input("\tChoose an option(1-3): ")
    match option:
        case "1":
            os.system('clear')
            designCalculateTax()
        case "2":
            os.system('clear')
            desginSeeList()
        case "3":
            os.system('clear')
            print("Thanks for using taxes calculator")
            sleep(1.5)
            break
        case _:
            print("Try again")