from menu.calculateTax import designCalculateTax
from menu.seeList import designSeeList
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
    
    if option == "1":
        designCalculateTax()
    elif option == "2":
        designSeeList()
    elif option == "3":
        os.system('clear')
        print("Thanks for using tax calculator")
        sleep(1.5)
        break
    else:
        print("\tInvalid option, try again")
        sleep(1.5)
