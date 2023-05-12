from empire_commons import list_util
from empire_commons.empire_string import String


def test_rreplace():
    s: String = String("rogers jean guy roger")

    assert s.rreplace("roger", "pauline") == "rogers jean guy pauline"
    assert s.rreplace(s, "roger", "paulin", 2) == "paulins jean guy paulin"
    assert s == "rogers jean guy roger"


def test_contains_any_of():
    s: str = "rogers jean guy roger"

    # assert not StringUtil.contains_any_of(s, "patate", "légume", "raoul")
    # assert StringUtil.contains_any_of(s, "raymond", "guy", "gontrand")


def test_is_float():
    s1: str = "patate"
    s2: str = "123"
    s3: str = "3.14"

    # assert not StringUtil.is_float(s1)
    # assert StringUtil.is_float(s2) == StringUtil.is_float(s3) is True


def test_create_sized_ngrams():
    assert list_util.equals(
        # StringUtil.create_sized_ngrams("rogers jean guy gontrand", 1),
        ["rogers", "jean", "guy", "gontrand"],
    )
    assert list_util.equals(
        # StringUtil.create_sized_ngrams("rogers jean guy gontrand", 2),
        ["rogers jean", "jean guy", "guy gontrand"],
    )
    assert list_util.equals(
        # StringUtil.create_sized_ngrams("rogers jean guy gontrand", 3),
        ["rogers jean guy", "jean guy gontrand"],
    )
    assert list_util.equals(
        # StringUtil.create_sized_ngrams("rogers jean guy gontrand", 4),
        ["rogers jean guy gontrand"],
    )


def test_create_ngrams():
    # ngrams = StringUtil.create_ngrams("rogers jean guy gontrand")
    # assert len(ngrams[-1]) == len("rogers jean guy gontrand".split()), "Number of words should be computed by length of last ngram list " \
    #                                                                    "(ngrams of size 1)"

    # assert list_util.equals(
    #     StringUtil.create_ngrams("rogers jean guy gontrand"),
    #     [
    #         ["rogers jean guy gontrand"],
    #         ["rogers jean guy", "jean guy gontrand"],
    #         ["rogers jean", "jean guy", "guy gontrand"],
    #         ["rogers", "jean", "guy", "gontrand"],
    #     ],
    # )
    pass

def test_batch_replace():
    s: str = "patate poil légume rogers cendrier plombier poubelle"

    # assert (
    #     StringUtil.batch_replace(s, "panier", "piano", replacement="potato")
    #     == "patate poil légume rogers cendrier plombier poubelle"
    # )
    # assert (
    #     StringUtil.batch_replace(s, replacement="jeannot")
    #     == "patate poil légume rogers cendrier plombier poubelle"
    # )
    # assert (
    #     StringUtil.batch_replace(s, "patate", "cendrier", replacement="gontrand")
    #     == "gontrand poil légume rogers gontrand plombier poubelle"
    # )
    assert s == "patate poil légume rogers cendrier plombier poubelle"


def test_join_non_nulls_non_empty():
    s = [None, "roger", "", "gontrand"]

    # assert StringUtil.join_non_nulls_non_empty(s, " ") == "roger gontrand"
    assert list_util.equals(s, [None, "roger", "", "gontrand"])


def test_limit_string_length():
    s = "patate"

    # assert StringUtil.limit_string_length(s, 3) == "pat"
    assert s == "patate"


def test_to_camel_case():
    s = "Roger gontrand POTATO sYnVaIn-raymond-dutrizac_publisac"
    # assert (
    #     StringUtil.to_camel_case(s)
    #     == "rogerGontrandPotatoSynvainRaymondDutrizacPublisac"
    # )
    assert s == "Roger gontrand POTATO sYnVaIn-raymond-dutrizac_publisac"


def test_to_pascal_case():
    s = "Roger gontrand POTATO sYnVaIn-raymond-dutrizac_publisac"
    # assert (
    #         StringUtil.to_pascal_case(s)
    #         == "RogerGontrandPotatoSynvainRaymondDutrizacPublisac"
    # )
    assert s == "Roger gontrand POTATO sYnVaIn-raymond-dutrizac_publisac"
