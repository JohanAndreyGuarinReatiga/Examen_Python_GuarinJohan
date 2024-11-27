import json

def read_file(path):
    try:
        with open(f"databases/{path}", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  
     
def write_file(data, path):
    with open(f"databases/{path}", "w") as file:
        json.dump(data, file, indent=4)

def save_file(person_data):
    write_file(person_data, "taxes.json")

def user_data(person_data, amount, category):
    if category not in person_data:
        person_data[category] = []
    person_data[category].append({
        "amount": amount,
    })
    return person_data

def calculationOne(amount, tax_rate):
    return amount * tax_rate / 100

def calculateTotalTaxes(person_data):
    totalTaxes = 0
    categoryTotal = {}
    for category, taxes in person_data.items():
        for tax in taxes:
            totalTaxes += tax["amount"] * 0.1 
            categoryTotal[category] = categoryTotal.get(category, 0) + tax["amount"]

    return totalTaxes, categoryTotal