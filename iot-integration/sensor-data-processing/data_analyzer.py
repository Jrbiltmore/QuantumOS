import json

def load_data(file_path):
    """
    Load data from a JSON file.
    
    :param file_path: Path to the JSON file.
    :return: Data loaded from the file.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def analyze_data(data):
    """
    Perform basic analysis on the data.
    
    :param data: The data to analyze, assumed to be a list of dictionaries.
    """
    if not data:
        print("No data provided.")
        return

    # Example analysis: count the records
    record_count = len(data)
    print(f"Total records: {record_count}")

    # Assuming data contains a numerical field named 'value' for demonstration
    total_value = sum(item.get('value', 0) for item in data)
    average_value = total_value / record_count if record_count > 0 else 0
    print(f"Average value: {average_value:.2f}")

def main():
    # Path to the JSON data file
    file_path = 'data.json'  # Update this to the path of your JSON data file
    
    # Load the data
    data = load_data(file_path)
    
    # Analyze the data
    analyze_data(data)

if __name__ == "__main__":
    main()
