cpdef str to_camel_case_strip_spaces(str the_string):
    cdef camel_case = to_pascal_case_strip_spaces(the_string)
    return camel_case[0].lower() + camel_case[1:]

cpdef str to_camel_case_with_underscores(str the_string):
    cdef camel_case = to_pascal_case_with_underscores(the_string)
    return camel_case[0].lower() + camel_case[1:]

cpdef str to_pascal_case_strip_spaces(str the_string):
    if not the_string:
        return the_string

    cdef words = (the_string
                  .replace(' ', ' ')
                  .replace('-', ' ')
                  .replace('.', ' ')
                  .replace(',', ' ')
                  .replace(':', ' ')
                  .replace(';', ' ')).split()

    cdef result = []
    for word in words:
        result.append(word.capitalize())

    cdef joint_result = ''.join(result)
    return joint_result

cpdef str to_pascal_case_with_underscores(str the_string):
    if not the_string:
        return the_string

    cdef words = (the_string
                  .replace(' ', ' ')
                  .replace('-', ' ')
                  .replace('.', ' ')
                  .replace(',', ' ')
                  .replace(':', ' ')
                  .replace(';', ' ')).split()

    cdef result = []
    for word in words:
        result.append(word.capitalize())

    cdef joint_result = '_'.join(result)
    return joint_result

cpdef str to_upper_case_with_underscores(str the_string):
    if not the_string:
        return the_string

    return the_string.upper()\
        .replace(' ', '_')\
        .replace('-', '_')\
        .replace('.', '_')\
        .replace(',', '_')\
        .replace(':', '_')\
        .replace(';', '_')
