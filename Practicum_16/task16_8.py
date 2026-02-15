from itertools import chain, combinations


def get_all_subsets(numbers_str: str) -> list:
    """
    Get all subsets of the given set.
    
    Args:
        numbers_str: String with space-separated natural numbers
    
    Returns:
        List of all subsets
    """
    numbers = list(map(int, numbers_str.split()))
    numbers.sort()
    
    subsets = []
    for r in range(len(numbers) + 1):
        for combo in combinations(numbers, r):
            subsets.append(list(combo))
    
    return subsets


def main():
    """
    Main function to demonstrate the functionality of get_all_subsets.
    """
    numbers_str = input("Введите множество чисел: ")
    
    subsets = get_all_subsets(numbers_str)
    
    print("Все подмножества:")
    for subset in subsets:
        print(subset)


if __name__ == '__main__':
    main()