import csv
import json

def csv_to_json(csv_file_path='profiles1.csv', json_file_path='data.json'):
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)

    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    csv_to_json()