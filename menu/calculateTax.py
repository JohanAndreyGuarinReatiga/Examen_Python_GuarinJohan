from logic.calculateTax import read_file, save_file, user_data, calculationOne
import os
from time import sleep

def designCalculateTax():
    person_data = read_file("databases/taxes.json")
    while True:
        print("""
        ---------------------------------------------------
                        TAXES CALCULATION
        ---------------------------------------------------
            Enter the amount of the product or service
        ---------------------------------------------------
        """)
        try:
            amount = float(input("\tEnter: "))
        except ValueError:
            print("\tInvalid, try again")
            sleep(1)
            continue
        
        print("""
        ---------------------------------------------------
        Choose the type of tax:
        1. IVA (10%)
        2. Special tax (5%)
        3. Local Tax (8%)
        4. Other 
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
            tax_description = "Special tax (5%)"
        elif category == "3":
            tax_rate = 8
            tax_description = "Local Tax (8%)"
        elif category == "4":
            try:
                custom_tax = float(input("\tEnter a percentage: "))
                tax_rate = custom_tax
                tax_description = f"Other ({custom_tax}%)"
            except ValueError:
                print("\tInvalid, try again.")
                sleep(1.5)
                continue
        elif category == "5":
            print("\tLeaving")
            save_file(person_data)
            break
        else:
            print("\tInvalid, try again")
            sleep(1.5)
            continue
        
        tax_amount = calculationOne(amount, tax_rate)
        total_amount = amount + tax_amount


        person_data = user_data(person_data, amount, tax_rate, tax_description, tax_amount, total_amount)
        print(f"""
        ---------------------------------------------------
                        Calculation result
        ---------------------------------------------------
        Base amount: ${amount}
        Tax(es):
        - {tax_description}: ${tax_amount}
        Total with taxes: ${total_amount}
        ---------------------------------------------------
        """)
        more_tax = input("\n\tDo you want to calculate again (1. yes / 2. no - go back): ")
        if more_tax == "2":
            print("\tgoing back\n")
            save_file(person_data)
            sleep(1.5)
            break