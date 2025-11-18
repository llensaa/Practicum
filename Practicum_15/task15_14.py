def numbers(x: int):
    """
    Print digits of natural number x in reverse order.
    
    Args:
        x: Natural number
    """
    if x < 10:
        print(x)
    else:
        print(x % 10)
        numbers(x // 10)


def main():
    """
    Main function to demonstrate the functionality of numbers.
    """
    x = int(input("Enter natural number: "))
    
    numbers(x)


if __name__ == '__main__':
    main()