from person import Person
import pytest

# @pytest.fixture
# def person():
#     return Person("Steve", "Nacke", 45)

def test_init():
    person = Person("Steve", "Nacke", 45)

    assert person._firstname == "Steve"
    assert person._lastname == "Nacke"
    assert person._age == 45
    assert person._inventory == []
    assert person._account == pytest.approx(1000.0)

def test_fullname():
    person = Person("Steve", "Nacke", 45)
    assert person.fullname == "Steve Nacke"

def test_can_buy_an_item():
    person = Person("Steve", "Nacke", 45)
    person.buy("Cigar", 5.0)
    assert person._inventory == ["Cigar"]
    assert person._account == pytest.approx(995.0)

def test_not_enough_money_raise_userwarning():
    person = Person("Steve", "Nacke", 45)
    with pytest.warns(UserWarning):
        person.buy("Car", 2000.0)
        assert person._inventory == []
        assert person._account == pytest.approx(1000.0)