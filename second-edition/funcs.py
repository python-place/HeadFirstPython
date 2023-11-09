def search4vowels(word: str) -> set:
    """Return any vowels found in a supplied word
    :rtype: set
    """
    vowels = set('aeiou')
    return vowels.intersection(set(word))
