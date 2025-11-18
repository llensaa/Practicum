def combin(n: int, k: int) -> int:
    """
    Compute the combinatorial combination C(n, k).
    
    Args:
        n: Total number of elements
        k: Number of elements to choose
    
    Returns:
        Number of combinations C(n, k)
    """
    if k == 0 or k == n:
        return 1
    else:
        return combin(n - 1, k - 1) + combin(n - 1, k)


def main():
    """
    Main function to demonstrate the functionality of combin.
    """
    n = int(input("Enter n: "))
    k = int(input("Enter k: "))
    
    result = combin(n, k)
    
    print(f"C({n}, {k}) = {result}")


if __name__ == '__main__':
    main()