import json
import os

def aggregate_data(file_paths):
    """
    Aggregates data from multiple JSON files and returns a combined dictionary.
    """
    aggregated_data = []

    for file_path in file_paths:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                aggregated_data.extend(data)
        else:
            print(f"File {file_path} not found.")
    
    return aggregated_data

def main():
    # List of JSON file paths to aggregate data from
    file_paths = ['data1.json', 'data2.json', 'data3.json']
    
    # Aggregating data
    aggregated_data = aggregate_data(file_paths)
    
    # Printing aggregated data
    print("Aggregated Data:")
    print(json.dumps(aggregated_data, indent=2))

if __name__ == "__main__":
    main()
