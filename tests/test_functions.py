from empire_commons.commons.functions import returns_on_falsy_first_parameter


@returns_on_falsy_first_parameter
def a_function(a, b):
    return 'patate'


def test_returns_on_falsy_first_parameter():
    assert a_function(None, 'patate') is None
    assert a_function('', 'patate') == ''
    assert a_function(0, 'patate') == 0
    assert a_function([], 'patate') == []
    assert a_function({}, 'patate') == {}
    assert a_function((), 'patate') == ()
    assert a_function('rogers', 'patate') == 'patate'

    assert a_function(None, b='rogers') is None

    assert a_function(a=None, b='rogers') is None
    assert a_function(a='', b='patate') == ''
    assert a_function(a=0, b='patate') == 0
    assert a_function(a=[], b='patate') == []
    assert a_function(a={}, b='patate') == {}
    assert a_function(a=(), b='patate') == ()
    assert a_function(a='raoul', b='rogers') == 'patate'
