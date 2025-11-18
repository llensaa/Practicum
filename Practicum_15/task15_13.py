def odd_list(a: list, n: int) -> list:
    """
    Return list of even values from the input list.
    
    Args:
        a: List of integers
        n: Number of elements in the list
    
    Returns:
        List containing only even values from a
    """
    if n == 0:
        return []
    else:
        rest = odd_list(a, n - 1)
        if a[n - 1] % 2 == 0:
            return rest + [a[n - 1]]
        else:
            return rest


def main():
    """
    Main function to demonstrate the functionality of odd_list.
    """
    a = list(map(int, input("Enter list elements: ").split()))
    n = len(a)
    
    result = odd_list(a, n)
    
    print(f"Even numbers: {result}")


if __name__ == '__main__':
    main()