
import pytest
from pet_boarding import boarding_fee, admission_ok, checkout_status


# 1. Boarding fee: valid and invalid inputs

def test_unknown_pet():
    with pytest.raises(ValueError, match="unknown pet type"):
        boarding_fee("hamster", 3, False)


def test_negative_days():
    with pytest.raises(ValueError, match="invalid days"):
        boarding_fee("cat", -1, False)


# 2. Included days and extra-day charges

def test_included_days_and_no_extra_fee():
    assert boarding_fee("cat", 3, False) == 0
    assert boarding_fee("dog", 2, False) == 0
    assert boarding_fee("rabbit", 4, False) == 0


def test_extra_day_rates():
    assert boarding_fee("cat", 5, False) == 40
    assert boarding_fee("dog", 4, False) == 60
    assert boarding_fee("rabbit", 6, False) == 40


# 3. Premium membership branches

def test_premium_membership():
    assert boarding_fee("cat", 4, True) == 0
    assert boarding_fee("dog", 3, True) == 0
    assert boarding_fee("rabbit", 5, True) == 20


# 4. High extra-day charges and nested dog condition

def test_high_extra_days():
    assert boarding_fee("cat", 14, False) == 330
    assert boarding_fee("dog", 13, False) == 495


# 5. Admission: senior and non-senior branches

def test_senior_admission():
    assert admission_ok(12, 3, True) is True
    assert admission_ok(12, 2, True) is False


def test_non_senior_age_branches():
    assert admission_ok(0, 3, False) is False
    assert admission_ok(2, 2, False) is True
    assert admission_ok(2, 1, False) is False


# 6. Checkout: open, late, and closed branches

def test_checkout_regular_day():
    assert checkout_status(15, False, False) == "open"
    assert checkout_status(10, False, False) == "late"
    assert checkout_status(-1, False, False) == "closed"


def test_checkout_long_stay():
    assert checkout_status(30, True, False) == "open"
    assert checkout_status(20, True, False) == "late"
    assert checkout_status(10, True, False) == "closed"


def test_checkout_weekend():
    assert checkout_status(35, False, True) == "open"
    assert checkout_status(20, False, True) == "late"
    assert checkout_status(19, False, True) == "closed"
