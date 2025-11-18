def ind_maxlist(a: list) -> int:
    """
    Find the index of the maximum element in a list of integers.
    
    Args:
        a: List of integers
    
    Returns:
        The index of the maximum element in the list
    """
    if len(a) == 1:
        return 0
    else:
        max_index_rest = ind_maxlist(a[1:]) + 1
        return 0 if a[0] > a[max_index_rest] else max_index_rest


def main():
    """
    Main function to demonstrate the functionality of ind_maxlist.
    """
    a = list(map(int, input("Enter list elements: ").split()))
    
    result = ind_maxlist(a)
    
    print(f"Index of maximum element: {result}")


if __name__ == '__main__':
    main()