cpdef list only_keep_these_root_keys(list the_list, list keys):
    return [
        {
            a_dict_key: a_dict_value
            for a_dict_key, a_dict_value in a_dict.items()
            if a_dict_key in keys
        }
        for a_dict in the_list
    ]


cpdef dict create_dict_from_list_of_dicts(list the_list, str key):
    return {item[key]: item for item in the_list}


cpdef dict create_dict_from_list_of_objects(list the_list, str key):
    return {getattr(item, key): item for item in the_list}

