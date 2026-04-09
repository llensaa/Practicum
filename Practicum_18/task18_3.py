def count_numbers_not_multiple_ending_with(a: int, b: int, c: int, d: int) -> int:
    """
    Counts natural numbers in interval [a; b] that are not multiples of c
    and end with digit d.
    
    Args:
        a: Start of interval
        b: End of interval
        c: Divisor to check
        d: Ending digit to match
    
    Returns:
        Count of numbers satisfying the conditions
    """
    numbers = range(a, b + 1)
    mapped_values = map(lambda x: 1 if x % c != 0 and x % 10 == d else 0, numbers)
    return sum(mapped_values)


def main():
    """
    Main function to demonstrate counting numbers with specific properties.
    """
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    d = int(input("d = "))
    
    result = count_numbers_not_multiple_ending_with(a, b, c, d)
    print(result)


if __name__ == '__main__':
    main()