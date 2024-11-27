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

def user_data(person_data, amount, tax_rate, tax_description, tax_amount, total_amount):
    if tax_description not in person_data:
        person_data[tax_description] = []
    person_data[tax_description].append({
        "amount": amount,
        "tax_rate": tax_rate,
        "tax_amount": tax_amount,
        "total_amount": total_amount
    })
    return person_data

def calculationOne(amount, tax_rate):
    return amount * tax_rate / 100