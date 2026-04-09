def sum_multiples(a: int, b: int, c: int, d: int) -> int:
    """
    Calculates sum of natural numbers in interval [a; b] 
    that are multiples of both c and d.
    
    Args:
        a: Start of interval
        b: End of interval
        c: First divisor
        d: Second divisor
    
    Returns:
        Sum of numbers divisible by both c and d
    """
    numbers = range(a, b + 1)
    filtered_numbers = filter(lambda x: x % c == 0 and x % d == 0, numbers)
    return sum(filtered_numbers)


def main():
    """
    Main function to demonstrate sum of multiples calculation.
    """
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    d = int(input("d = "))
    
    result = sum_multiples(a, b, c, d)
    print(result)


if __name__ == '__main__':
    main()