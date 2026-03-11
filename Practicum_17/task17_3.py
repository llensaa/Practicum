def create_antonym_dictionary(pairs: list) -> dict:
    """
    Creates an antonym dictionary from pairs of words.
    
    Args:
        pairs: List of strings containing antonym word pairs
    
    Returns:
        Dictionary with words as keys and their antonyms as values
    """
    antonyms = {}
    
    for pair in pairs:
        word1, word2 = pair.split()
        antonyms[word1] = word2
        antonyms[word2] = word1
    
    return antonyms


def find_antonym(word: str, antonyms: dict) -> str:
    """
    Finds the antonym of a word using the provided dictionary.
    If the word is not found in the dictionary, it remains unchanged.
    
    Args:
        word: Word to find antonym for
        antonyms: Dictionary mapping words to their antonyms
    
    Returns:
        Antonym of the word if found, otherwise the original word
    """
    if word in antonyms:
        return antonyms[word]
    else:
        return word


def main():
    """
    Main function to demonstrate antonym lookup.
    """
    n = int(input())
    pairs = []

    for _ in range(n):
        pair = input()
        pairs.append(pair)
    
    antonyms = create_antonym_dictionary(pairs)
    word = input()
    result = find_antonym(word, antonyms)
    print(result)


if __name__ == '__main__':
    main()