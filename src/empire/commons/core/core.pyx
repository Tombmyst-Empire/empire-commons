cpdef dict dict_util_swap_key_values(dict the_dict):
    """
    Swap a dictionary keys and values
    """
    return {value: key for key, value in the_dict.items()}


cpdef dict dict_util_remap(dict the_dict, dict mapping):
    """
    Remaps the given directory using the provided mapping.

    The mapping keys represent the provided dictionary keys and mapping values represent
    the desired keys.
    """
    return {
        mapping.get(key, key): value
        for key, value in the_dict.items()
    }


cpdef dict_util_get_first_non_null(dict the_dict, tuple fields, default = None):
    """
    Returns the first non-None value from a sequence of fields of a dictionary.
    If none of the fields returned a non-None value, then the method return *default*.

    """
    for field in fields:
        if the_dict.get(field):
            return the_dict[field]
    return default


cpdef dict dict_util_try_del(dict the_dict, object key):
    """
    Tries to delete a fields from a dictionary.
    """
    if key in the_dict:
        del the_dict[key]

