from empire_commons import list_util


def test_equals():
    l1 = [1, 2, 3]
    l2 = [1, 2, 3]
    l3 = [1, 2, 4]
    l4 = [3, 2, 1]

    assert list_util.equals(l1, l2, ignore_order=True)
    assert list_util.equals(l1, l2, ignore_order=False)
    assert list_util.equals(l1, l4, ignore_order=True)
    assert not list_util.equals(l1, l4, ignore_order=False)
    assert not list_util.equals(l1, l3, ignore_order=True)
    assert not list_util.equals(l1, l3, ignore_order=False)


def test_equals_nested_lists():
    l = [[1, 2, 3], [4, 5, 6]]

    assert list_util.equals(l, [[1, 2, 3], [4, 5, 6]])
    assert list_util.equals(l, [[1, 2, 3], [4, 5, 6]], ignore_order=False)


def test_try_get():
    l = ["patate", "roger"]

    assert list_util.try_get(l, 4, "simon") == "simon"
    assert list_util.try_get(l, 1, "raoul") == "roger"
    assert list_util.equals(l, ["patate", "roger"]), "original list must not change"


def test_contains_sub_list_does_not_contain():
    a1 = ["patate", "légume", "aubergine"]
    a2 = ["cocombre", "tomato", "potato", "petit pois"]

    assert list_util.contains_sub_list(a1, a2) == list_util.contains_sub_list(a2, a1)
    assert list_util.contains_sub_list(a1, a2) is False
    assert list_util.equals(
        a1, ["patate", "légume", "aubergine"]
    ), "original list must not change"
    assert list_util.equals(
        a2, ["cocombre", "tomato", "potato", "petit pois"]
    ), "original list must not change"


def test_contains_sub_list_contains():
    b1 = ["roger", "raoul", "raymonde", "rododendron"]
    b2 = [
        "simonette",
        "roger",
        "gérard",
        "balthazar",
        "raoul",
        "jean-guy-roger",
        "raymonde",
        "gontrand",
        "rododendron",
    ]

    assert list_util.contains_sub_list(b1, b2) == list_util.contains_sub_list(b2, b1)
    assert list_util.contains_sub_list(b1, b2) is True
    assert list_util.equals(
        b1, ["roger", "raoul", "raymonde", "rododendron"]
    ), "original list must not change"
    assert list_util.equals(
        b2,
        [
            "simonette",
            "roger",
            "gérard",
            "balthazar",
            "raoul",
            "jean-guy-roger",
            "raymonde",
            "gontrand",
            "rododendron",
        ],
    ), "original list must not change"


def test_filter_string_list_ignore_case():
    l = ["aBc", "Bcd", "cdE", "Def", "aCe", "bdF", "Deb"]

    r = list_util.filter_list_of_strings(l, must_start_with=("z",), ignore_case=True)
    assert len(r) == 0

    r = list_util.filter_list_of_strings(l, must_start_with=("c",), ignore_case=True)
    assert len(r) == 1
    assert "cdE" in r

    r = list_util.filter_list_of_strings(l, must_start_with=("a", "b"), ignore_case=True)
    assert len(r) == 4
    assert "aBc" in r
    assert "Bcd" in r
    assert "aCe" in r
    assert "bdF" in r

    r = list_util.filter_list_of_strings(l, must_end_with=("z",), ignore_case=True)
    assert len(r) == 0

    r = list_util.filter_list_of_strings(l, must_end_with=("c",), ignore_case=True)
    assert len(r) == 1
    assert "aBc" in r

    r = list_util.filter_list_of_strings(l, must_end_with=("e", "f"), ignore_case=True)
    assert len(r) == 4
    assert "cdE" in r
    assert "Def" in r
    assert "aCe" in r
    assert "bdF" in r

    r = list_util.filter_list_of_strings(l, must_contain=("z",), ignore_case=True)
    assert len(r) == 0

    r = list_util.filter_list_of_strings(l, must_contain=("B",), ignore_case=True)
    assert len(r) == 4
    assert "aBc" in r
    assert "Bcd" in r
    assert "bdF" in r
    assert "Deb" in r

    r = list_util.filter_list_of_strings(l, must_contain=("e", "D"), ignore_case=True)
    assert len(r) == 6
    assert "Bcd" in r
    assert "cdE" in r
    assert "Def" in r
    assert "aCe" in r
    assert "bdF" in r
    assert "Deb" in r

    assert list_util.equals(
        l, ["aBc", "Bcd", "cdE", "Def", "aCe", "bdF", "Deb"]
    ), "original list must not change"


def test_filter_string_list_with_case():
    l = ["aBc", "Bcd", "cdE", "Def", "aCe", "bdF", "Deb"]

    r = list_util.filter_list_of_strings(l, must_start_with=("z",), ignore_case=False)
    assert len(r) == 0

    r = list_util.filter_list_of_strings(l, must_start_with=("c",), ignore_case=False)
    assert len(r) == 1
    assert "cdE" in r

    r = list_util.filter_list_of_strings(l, must_start_with=("a", "b"), ignore_case=False)
    assert len(r) == 3
    assert "aBc" in r
    assert "aCe" in r
    assert "bdF" in r

    r = list_util.filter_list_of_strings(l, must_end_with=("z",), ignore_case=False)
    assert len(r) == 0

    r = list_util.filter_list_of_strings(l, must_end_with=("c",), ignore_case=False)
    assert len(r) == 1
    assert "aBc" in r

    r = list_util.filter_list_of_strings(l, must_end_with=("e", "f"), ignore_case=False)
    assert len(r) == 2
    assert "Def" in r
    assert "aCe" in r

    r = list_util.filter_list_of_strings(l, must_contain=("z",), ignore_case=False)
    assert len(r) == 0

    r = list_util.filter_list_of_strings(l, must_contain=("B",), ignore_case=False)
    assert len(r) == 2
    assert "aBc" in r
    assert "Bcd" in r

    r = list_util.filter_list_of_strings(l, must_contain=("E", "D"), ignore_case=False)
    assert len(r) == 3
    assert "cdE" in r
    assert "Def" in r
    assert "Deb" in r

    assert list_util.equals(
        l, ["aBc", "Bcd", "cdE", "Def", "aCe", "bdF", "Deb"]
    ), "original list must not change"





def expansion_function(index: int):
    return index + 1


def test_expand_right():
    l = [1]

    assert tuple(list_util.expand_right(l, expansion_size=3, filler="patate")) == (
        1,
        "patate",
        "patate",
        "patate",
    )
    assert tuple(
        list_util.expand_right(l, expansion_size=5, filler=expansion_function)
    ) == (1, 1, 2, 3, 4, 5)
    assert len(l) == 1 and l[0] == 1, "original list must not change"


def test_expand_left():
    l = [1]

    assert tuple(list_util.expand_left(l, expansion_size=3, filler="patate")) == (
        "patate",
        "patate",
        "patate",
        1,
    )
    assert tuple(
        list_util.expand_left(l, expansion_size=5, filler=expansion_function)
    ) == (1, 2, 3, 4, 5, 1)
    assert len(l) == 1 and l[0] == 1, "original list must not change"


def test_zip_flattened():
    l1 = ['rogers', 'raymond', 'gontrand']
    l2 = ['natacha', 'germaine', 'bérangère']

    assert list_util.zip_flattened(l1, l2) == ['rogers', 'natacha', 'raymond', 'germaine', 'gontrand', 'bérangère']


def test_chunk_list():
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert list_util.chunk_list(l, 2) == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
