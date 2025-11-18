def maxlist(a: list) -> int:
    """
    Find the maximum element in a list of integers.
    
    Args:
        a: List of integers
    
    Returns:
        The maximum element in the list
    """
    if len(a) == 1:
        return a[0]
    else:
        rest_max = maxlist(a[1:])
        return a[0] if a[0] > rest_max else rest_max


def main():
    """
    Main function to demonstrate the functionality of maxlist.
    """
    a = list(map(int, input("Enter list elements: ").split()))
    
    result = maxlist(a)
    
    print(f"Maximum element: {result}")


if __name__ == '__main__':
    main()