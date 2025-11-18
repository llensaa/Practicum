def search(a: list, x: int) -> int:
    """
    Search for number x in list a.
    
    Args:
        a: List of integers
        x: Number to search for
    
    Returns:
        1 if x is found in a, 0 otherwise
    """
    if len(a) == 0:
        return 0
    elif a[0] == x:
        return 1
    else:
        return search(a[1:], x)


def main():
    """
    Main function to demonstrate the functionality of search.
    """
    a = list(map(int, input("Enter list elements: ").split()))
    x = int(input("Enter number to search: "))
    
    result = search(a, x)
    
    if result == 1:
        print(f"Number {x} was found")
    else:
        print(f"Number {x} was not found")


if __name__ == '__main__':
    main()