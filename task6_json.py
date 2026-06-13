import json

products_data = [
    {"name": "Laptop", "price": 75000, "quantity": 5},
    {"name": "Mouse", "price": 500, "quantity": 20},
    {"name": "Keyboard", "price": 1200, "quantity": 10}
]

file = open("products.json", "w")
json.dump(products_data, file, indent=4)
file.close()

print("JSON file created ")


file = open("products.json", "r")
products = json.load(file)
file.close()


print("\n{:<15} {:<10} {:<10}".format("Name", "Price", "Quantity"))
print("-" * 40)

for product in products:
    print("{:<15} {:<10} {:<10}".format(
        product["name"],
        product["price"],
        product["quantity"]
    ))