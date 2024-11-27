

def seeList():
    tax_list = [
        {"name": "IVA", "rate": 10},
        {"name": "Special tax", "rate": 5},
        {"name": "Local tax", "rate": 8},
        {"name": "Other", "rate": "personalized"}
    ]
    
    print("\ntypes of taxes:")
    for tax in tax_list:
        print(f"{tax['name']} ({tax['rate']}%)")
