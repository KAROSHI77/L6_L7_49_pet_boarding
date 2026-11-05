
import pytest
from pet_boarding import boarding_fee, admission_ok, checkout_status


# Boarding fee tests

def test_included_days():
    assert boarding_fee("cat", 3, False) == 0
    assert boarding_fee("dog", 2, False) == 0
    assert boarding_fee("rabbit", 4, False) == 0


def test_extra_days():
    assert boarding_fee("cat", 5, False) == 40
    assert boarding_fee("dog", 4, False) == 60
    assert boarding_fee("rabbit", 6, False) == 40


def test_premium_membership():
    assert boarding_fee("cat", 4, True) == 0
    assert boarding_fee("dog", 3, True) == 0
    assert boarding_fee("rabbit", 5, True) == 20


def test_high_extra_days():
    assert boarding_fee("cat", 14, False) == 330
    assert boarding_fee("dog", 13, False) == 495


def test_invalid_pet_type():
    with pytest.raises(ValueError, match="unknown pet type"):
        boarding_fee("hamster", 2, False)


def test_negative_days():
    with pytest.raises(ValueError, match="invalid days"):
        boarding_fee("cat", -1, False)


# Admission tests

def test_senior_admission():
    assert admission_ok(12, 3, True) is True
    assert admission_ok(12, 2, True) is False


def test_non_senior_admission():
    assert admission_ok(0, 3, False) is False
    assert admission_ok(2, 2, False) is True
    assert admission_ok(2, 1, False) is False


# Checkout tests

def test_checkout_open():
    assert checkout_status(15, False, False) == "open"
    assert checkout_status(30, True, False) == "open"
    assert checkout_status(35, False, True) == "open"


def test_checkout_late():
    assert checkout_status(0, False, False) == "late"
    assert checkout_status(20, False, True) == "late"


def test_checkout_closed():
    assert checkout_status(-1, False, False) == "closed"
    assert checkout_status(10, False, True) == "closed"
