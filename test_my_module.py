from my_module import can_buy_alc
import pytest

def test_underaged_can_buy_non_alcoholic():
    expected = True
    returned = can_buy_alc(10, 0)
    assert returned == expected

def test_underaged_cannot_buy_any_alcoholic():
    expected = False
    returned = can_buy_alc(10, 5)
    assert returned == expected

def test_underaged_cannot_buy_any_alcoholic2():
    expected = False
    returned = can_buy_alc(10, 50)
    assert returned == expected

@pytest.mark.parametrize(
    "age,alc_pct,expected",
    [
        (10, 0, True),
        (10, 5, False),
        (18, 0, True),
        (18, 5, True),
        (18, 21, True),
        (18, 22, False),
        (20, 0, True),
        (20, 5, True),
        (20, 21, True),
        (20, 22, True),
        (20, 23, True),
    ]
)
def test_person_can_buy_or_not(age, alc_pct, expected):
    returned = can_buy_alc(age, alc_pct)
    assert returned == expected