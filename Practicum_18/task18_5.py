from functools import reduce


def product_of_perfect_squares_multiples(a: int, b: int, c: int) -> int:
    """
    Calculates product of natural numbers in interval [a; b] 
    that are perfect squares and multiples of c.
    
    Args:
        a: Start of interval
        b: End of interval
        c: Divisor to check
    
    Returns:
        Product of numbers satisfying conditions, 0 if no such numbers exist
    """
    numbers = range(a, b + 1)
    perfect_squares = [x for x in numbers if int(x ** 0.5) ** 2 == x and x % c == 0]
    
    if not perfect_squares:
        return 0
    
    return reduce(lambda x, y: x * y, perfect_squares, 1)


def main():
    """
    Main function to demonstrate product calculation.
    """
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    
    result = product_of_perfect_squares_multiples(a, b, c)
    print(result)


if __name__ == '__main__':
    main()