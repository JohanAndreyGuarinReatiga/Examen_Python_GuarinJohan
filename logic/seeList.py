

def seeList():
    tax_list = [
        {"name": "IVA", "rate": 10},
        {"name": "Impuesto Especial", "rate": 5},
        {"name": "Impuesto Local", "rate": 8},
        {"name": "Otro", "rate": "personalizado"}
    ]
    
    print("\nTipos de Impuestos:")
    for tax in tax_list:
        print(f"{tax['name']} ({tax['rate']}%)")
