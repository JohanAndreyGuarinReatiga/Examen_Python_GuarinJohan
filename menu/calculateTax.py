from logic.calculateTax import read_file, save_file, user_data, calculationOne
import os 
from time import sleep

#Ingrese el valor del impuesto (en porcentaje) si seleccionó "Otro":
#> [Usuario ingresa valor o selecciona uno predefinido]
#---------------------------------------------------
#¿Desea agregar otro impuesto?
#1. Sí
#2. No
#--------------------------------------------------

def designCalculateTax():
    person_data = read_file("taxes.json")
    while True:
        os.system('clear')
        print("""
        ---------------------------------------------------
                          TAX CALCULATION
        ---------------------------------------------------
            Enter the amount of the product or the service
        ---------------------------------------------------
""")
        amount = input(f"""\tTax amount: """).upper()
        try:
            amount = float(amount)
        except ValueError:
            print("\tinvalid amount, please enter a valid number")
            sleep(1.5)
            continue
        print("""
        ---------------------------------------------------
        Choose the tax type:
        1. IVA (10%)
        2. Especial Tax (5%)
        3. Local Tax (8%)
        4. Other (enter a personalized tax)
        ---------------------------------------------------
""")
        category = input("\tChoose an option(1-4): ")
        match category:
            case 1:
                continue
                #calculationOne()
            
        comment = input("\tEnter a brief description: ")
        print("press 's' to save or 'c' to cancel")
        if amount == "S":
            print("\tLeaving and saving data")
            save_file(person_data)
            sleep(1.5)
            os.system('clear')
            break
        elif amount == "C":
            os.system('clear')
            break
        try:
            person_data = user_data(person_data, amount, category, comment)
            print(f"\tTax succesfully registered")
        except ValueError as e:
            print(e)

designCalculateTax()
