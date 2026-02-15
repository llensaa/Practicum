def only_sladkoezhkin_likes(sladkoezhkin: str, N: int, friends_preferences: list) -> int:
    """
    Determine how many products only Sladkoezhkin likes.
    
    Args:
        sladkoezhkin: String with Sladkoezhkin's preferences
        N: Number of friends
        friends_preferences: List of strings with friends' preferences
    
    Returns:
        Number of products only Sladkoezhkin likes
    """
    sladkoezhkin_likes = set(sladkoezhkin.split())
    friends_like = set(" ".join(friends_preferences).split())
    
    only_sladkoezhkin = sladkoezhkin_likes - friends_like
    
    return f"{len(only_sladkoezhkin)} ({', '.join(only_sladkoezhkin)})"


def main():
    """
    Main function to demonstrate the functionality of only_sladkoezhkin_likes.
    """
    sladkoezhkin = input("Введите предпочтения Сладкоежкина: ")
    N = int(input("Введите количество друзей: "))
    
    friends_preferences = []
    for i in range(N):
        pref = input(f"Введите предпочтения друга {i + 1}: ")
        friends_preferences.append(pref)
    
    result = only_sladkoezhkin_likes(sladkoezhkin, N, friends_preferences)
    
    print(f"Количество продуктов, которые нравятся только Сладкоежкину: {result}")


if __name__ == '__main__':
    main()