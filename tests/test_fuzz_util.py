from empire.commons import fuzz_util


def test_get_highest_scoring():
    l = ["roger", "raymond", "raoul", "régis", "réglisse"]
    assert fuzz_util.get_highest_scoring_string("rogers", *l) == "roger"


def test_get_average():
    assert int(fuzz_util.get_fuzz_average("roger", "rogers")) == 90
    assert int(fuzz_util.get_fuzz_average("roger", "patate")) == 18
