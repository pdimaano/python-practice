def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    modified_phrase = ""
    for letter in phrase:
        if letter == to_swap.lower():
            modified_phrase += letter.upper()
        elif letter == to_swap.upper():
            modified_phrase += letter.lower()
        else:
            modified_phrase += letter

    return modified_phrase