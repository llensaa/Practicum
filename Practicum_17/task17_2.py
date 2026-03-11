def create_dictionary(pairs: list) -> dict:
    """
    Creates a Russian-English dictionary from pairs of words.
    
    Args:
        pairs: List of strings containing Russian-English word pairs
    
    Returns:
        Dictionary with Russian words as keys and English translations as values
    """
    dictionary = {}
    
    for pair in pairs:
        words = pair.split()
        if len(words) == 2:
            russian, english = words
            dictionary[russian] = english
    
    return dictionary


def translate_phrase(phrase: str, dictionary: dict) -> str:
    """
    Translates a Russian phrase to English using the provided dictionary.
    Words not found in the dictionary remain unchanged.
    
    Args:
        phrase: Russian phrase to translate
        dictionary: Russian-English dictionary
    
    Returns:
        Translated phrase with unknown words kept in Russian
    """
    words = phrase.split()
    translated_words = []
    
    for word in words:
        if word in dictionary:
            translated_words.append(dictionary[word])
        else:
            translated_words.append(word)
    return ' '.join(translated_words)


def main():
    """
    Main function to demonstrate Russian-English phrase translation.
    """
    n = int(input())

    pairs = []
    for _ in range(n):
        pair = input()
        pairs.append(pair)

    russian_english = create_dictionary(pairs)
    phrase = input()
    result = translate_phrase(phrase, russian_english)
    print(result)


if __name__ == '__main__':
    main()