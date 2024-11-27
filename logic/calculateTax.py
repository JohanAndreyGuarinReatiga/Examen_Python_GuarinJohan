import json

def read_file(path):
    with open(f"databases/{path}", "r") as file:
        return json.load(file)

def write_file(data, path):
    with open(f"databases/{path}", "w") as file:
        json.dump(data, file, indent=4)

def save_file(person_data):
    write_file(person_data, "taxes.json")
    
def user_data(person_data, amount, category, comment):
    if category not in person_data:
        person_data[category] = []
    person_data[category].append({
        "amount": amount,
        "description": comment,
    })
    return person_data

def calculationOne():
    pass


def calculateTotalTaxes(person_data):
    totalTaxes = 0
    categoryTotal = {}
    for category, taxes in person_data.items():
        for amount in taxes:
            try:
                totalTaxes += amount["amount"]
                categoryTotal[category] = categoryTotal.get(category, 0) + amount["amount"]
            except ValueError:
                continue
    
    return totalTaxes, categoryTotal