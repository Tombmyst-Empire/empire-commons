def zip_flattened(*items_to_zip: list) -> list:
    """
    As doing ``zip(list1, list2)`` will create a list of tuples, this function performs the zip operation
    and flattens the list.

    Example: ::

        l = [1, 3, 5]
        ll = [2, 4, 6]
        print(ListUtil.zip_flattened(l, ll))

        # >>> [1, 2, 3, 4, 5, 6]
        # instead of:
        # [(1, 2), (3, 4), (5, 6)]
    """
    return [sub_zip for zipped in zip(*items_to_zip) for sub_zip in zipped]
