def count(n: int) -> int:
    """
    Count the number of digits in a natural number using division by 10.
    
    Args:
        n: A natural number
    
    Returns:
        The number of digits in the given number
    """
    if n < 10:
        return 1
    else:
        return 1 + count(n // 10)


def main():
    """
    Main function to demonstrate the functionality of count.
    """
    n = int(input("Enter a natural number: "))
        
    if n < 0:
        print("Please enter a natural number")
        return
        
    result = count(n)
    print(f"Number {n} has {result} digits")


if __name__ == '__main__':
    main()