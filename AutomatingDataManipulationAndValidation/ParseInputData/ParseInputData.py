import csv
import json
import xml.etree.ElementTree as ET

# Open .txt file for groceries
file_path_txt = "groceries.txt"

with open(file_path_txt, "r") as file:
    data = file.read()

# Show the data in the .txt file
print("data:", data)

# Parse and show the data in the .txt file
parsed_data = data.split(", ")
print("parsed data:", parsed_data)

# Show the third item in the list
print("item at index 2:", parsed_data[2])

# Open .csv file for groceries
file_path_csv = "groceries.csv"

# Parse and show the data in the .csv file
with open(file_path_csv, "r") as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)
    for row in csv_reader:
        row[1] = int(row[1])
        print(row)

# Open .json file for groceries
file_path_json = "groceries.json"

# Parse the data in the .json file
with open(file_path_json, "r") as file:
    data = file.read()

parsed_data = json.loads(data)

# Show the quantity of apples in the list
print("apples quantity:", parsed_data["apples"])

# Open .xml file for groceries
file_path_xml = "groceries.xml"

# Parse the data in the .xml file
tree = ET.parse(file_path_xml)
root = tree.getroot()

# Show the items with prices higher than 6
items_over_6 = []

for item in root.findall("grocery_item"):
    name = item.find("name").text
    price = item.find("price").text
    if float(price) > 6.00:
        items_over_6.append(name)
    print(name, price)

print("items with prices higher that 6:", items_over_6)
