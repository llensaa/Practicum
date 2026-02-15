from itertools import permutations


def get_permutations(numbers_str: str) -> list:
    """
    Get all permutations of the set in lexicographic order.
    
    Args:
        numbers_str: String with space-separated natural numbers
    
    Returns:
        List of all permutations in lexicographic order
    """
    numbers = list(map(int, numbers_str.split()))
    numbers.sort()
    
    perms = list(permutations(numbers))
    
    return [list(perm) for perm in perms]


def main():
    """
    Main function to demonstrate the functionality of get_permutations.
    """
    numbers_str = input("Введите множество чисел: ")
    
    permutations_list = get_permutations(numbers_str)
    
    print("Все перестановки в лексикографическом порядке:")
    for perm in permutations_list:
        print(perm)


if __name__ == '__main__':
    main()