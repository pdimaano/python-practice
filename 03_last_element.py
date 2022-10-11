def last_element(lst):
    """Return last item in list (None if list is empty.

        >>> last_element([1, 2, 3])
        3

        >>> last_element([]) is None
        True
    """
    # python automatically returns None if there wasn't a return statement

    if len(lst) == 0:
        return None
    else:
        return lst[len(lst)-1]
