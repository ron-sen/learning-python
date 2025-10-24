import json
import csv
import os

INPUT_FILE = "api_data.json"
OUTPUT_FILE = "converted_data.csv"

def load_json_data(filename):
    if not os.path.exists(filename):
        print("JSON file not found")
        return []
    
    with open(filename, 'r', encoding="utf-8") as f:
        try:
            data = json.load(f)
            return data.get("students", [])  # Access the list of students
        except json.JSONDecodeError:
            print("Invalid JSON format")
            return []

def convert_to_csv(data, output_file):
    if not data:
        print("No data to convert")
        return

    # Flatten address for CSV
    fieldnames = list(data[0].keys())
    if "address" in fieldnames:
        fieldnames.remove("address")
        fieldnames.extend(["street", "city", "state", "zip"])

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for record in data:
            row = record.copy()
            if "address" in row:
                row.update(row.pop("address"))  # Flatten nested dict
            writer.writerow(row)

    print(f"Converted {len(data)} records to {output_file}")

def main():
    print("Converting JSON to CSV....")
    data = load_json_data(INPUT_FILE)
    convert_to_csv(data, OUTPUT_FILE)

if __name__ == "__main__":
    main()



