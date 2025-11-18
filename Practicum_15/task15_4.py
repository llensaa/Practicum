def sum_progress(a1: int, r: int, n: int) -> int:
    """
    Find the sum of the arithmetic progression.
    
    Args:
        a1: The first term of the arithmetic progression
        r: The common difference of the arithmetic progression
        n: The length of the arithmetic progression
    
    Returns:
        The sum of the arithmetic progression
    """
    if n == 1:
        return a1
    else:
        return ((a1 + (n - 1) * r) + sum_progress(a1, r, n - 1))


def main():
    """
    Main function to demonstrate the functionality of sum_progress.
    """
    a1 = int(input("Enter the first term: "))
    r = int(input("Enter the common difference: "))
    n = int(input("Enter the length of the arithmetic progression: "))
        
    result = sum_progress(a1, r, n)

    print(f"The sum of the arithmetic progression: S = {result}")


if __name__ == '__main__':
    main()