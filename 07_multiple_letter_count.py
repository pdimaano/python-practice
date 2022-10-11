def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    frequency_obj = {}

    for letter in phrase:
        count = 0 if (letter not in frequency_obj) else frequency_obj[letter]
        frequency_obj[letter] = count + 1
    return frequency_obj


