from logic.calculateTax import read_file, save_file, user_data, calculationOne
import os
from time import sleep

def designCalculateTax():
    person_data = read_file("taxes.json")
    while True:
        print("""
        ---------------------------------------------------
                          TAX CALCULATION
        ---------------------------------------------------
            Enter the amount of the product or the service
        ---------------------------------------------------
        """)
        try:
            amount = float(input("\tEnter amount: "))
        except ValueError:
            print("\tInvalid amount, please enter a valid number.")
            sleep(1.5)
            continue
        
        print("""
        ---------------------------------------------------
        Choose the tax type:
        1. IVA (10%)
        2. Especial Tax (5%)
        3. Local Tax (8%)
        4. Other (enter a personalized tax)
        5. Go back
        ---------------------------------------------------
        """)
        category = input("\tChoose an option (1-5): ")
        tax_rate = 0
        tax_description = ""

        if category == "1":
            tax_rate = 10
            tax_description = "IVA (10%)"
        elif category == "2":
            tax_rate = 5
            tax_description = "Especial Tax (5%)"
        elif category == "3":
            tax_rate = 8
            tax_description = "Local Tax (8%)"
        elif category == "4":
            try:
                custom_tax = float(input("\tIngrese un valor en porcentaje: "))
                tax_rate = custom_tax
                tax_description = f"Otro ({custom_tax}%)"
            except ValueError:
                print("\tValor de impuesto inválido, por favor intente de nuevo.")
                sleep(1.5)
                continue
        elif category == "5":
            print("\tRegresando al menú principal...")
            save_file(person_data)
            break
        else:
            print("\tOpción inválida, por favor intente de nuevo.")
            sleep(1.5)
            continue
        
        person_data = user_data(person_data, amount, tax_description)
        print(f"\tImpuesto registrado con éxito: {tax_description} sobre monto {amount}")

        more_tax = input("\n\t¿Desea agregar otro impuesto? (s/n): ")
        if more_tax.lower() == "n":
            print("\tFinalizando el cálculo de impuestos...\n")
            sleep(1.5)