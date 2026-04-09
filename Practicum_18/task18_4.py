import json


def sort_by_numeric_descending(data: list) -> list:
    """
    Sorts a list of lists by numeric values in descending order.
    
    Args:
        data: List of lists where first element is string, second is number
    
    Returns:
        Sorted list by numeric values in non-increasing order
    """
    return sorted(data, key=lambda x: x[1], reverse=True)


def main():
    """
    Main function to demonstrate sorting of JSON data.
    """
    json_string = input("Enter JSON list: ")
    data = json.loads(json_string)
    
    sorted_data = sort_by_numeric_descending(data)
    print(sorted_data)


if __name__ == '__main__':
    main()