def comp(a: str, b: str, m: int, n: int) -> int:
    """
    Find the length of the longest common subsequence of two strings.
    
    Args:
        a: First string
        b: Second string
        m: Length of first string
        n: Length of second string
    
    Returns:
        Length of the longest common subsequence
    """
    if m == 0 or n == 0:
        return 0
    elif a[m - 1] == b[n - 1]:
        return 1 + comp(a, b, m - 1, n - 1)
    else:
        return max(comp(a, b, m - 1, n), comp(a, b, m, n - 1))


def main():
    """
    Main function to demonstrate the functionality of comp.
    """
    a = input("Enter first string: ")
    b = input("Enter second string: ")
    
    result = comp(a, b, len(a), len(b))
    
    print(f"Length of longest common subsequence: {result}")


if __name__ == '__main__':
    main()