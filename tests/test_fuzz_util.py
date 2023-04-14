from empire.commons.fuzz_util import get_highest_scoring_string, get_fuzz_average


def test_get_highest_scoring():
    l = ["roger", "raymond", "raoul", "régis", "réglisse"]
    assert get_highest_scoring_string("rogers", l) == "roger"


def test_get_average():
    assert int(get_fuzz_average("roger", "rogers")) == 90
    assert int(get_fuzz_average("roger", "patate")) == 18
