import os
import csv
import json

INPUT_FILE = "raw_data.csv"
OUTPUT_FILE = "Converted_data.json"

def load_csv_data(filename):
    if not os.path.exists(filename):
        print("CSV file not found")
        return []
    
    with open(filename, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            # Strip extra spaces from keys and values
            row = {k.strip(): v.strip() for k, v in row.items()}
            # Convert 'is_active' to boolean
            if 'is_active' in row:
                row['is_active'] = row['is_active'].lower() == 'true'
            data.append(row)
    return data

def save_json_data(data, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")

# Load CSV and convert to JSON
data = load_csv_data(INPUT_FILE)
save_json_data(data, OUTPUT_FILE)
