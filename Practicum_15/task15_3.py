def progress(a1: int, r: int, n: int) -> int:
    """
    Find the n-th term of an arithmetic progression.
    
    Args:
        a1: The first term of the arithmetic progression
        r: The common difference of the arithmetic progression
        n: The position of the term to find
    
    Returns:
        The n-th term of the arithmetic progression
    """
    if n == 1:
        return a1
    else:
        return (r + progress(a1, r, n - 1))


def main():
    """
    Main function to demonstrate the functionality of progress.
    """
    a1 = int(input("Enter the first term: "))
    r = int(input("Enter the common difference: "))
    n = int(input("Enter the term position: "))
        
    result = progress(a1, r, n)

    print(f"The {n}-th term is: a_{n} = {result}")


if __name__ == '__main__':
    main()