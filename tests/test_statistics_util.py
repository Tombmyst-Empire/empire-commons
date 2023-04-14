from empire.commons.statistics_util import StatisticsUtil


def test_safe_fmean():
    assert StatisticsUtil.safe_fmean([1, 2, 3]) == 2.0
    assert StatisticsUtil.safe_fmean(None) == StatisticsUtil.safe_fmean([]) == 0.0
