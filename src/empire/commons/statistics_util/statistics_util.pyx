from statistics import fmean, mean as py_mean


cpdef double avg(list data):
    with nogil:
        if not data:
            return 0.0

    try:
        return fmean(data)
    except Exception:
        return py_mean(data)
