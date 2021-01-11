import pytest

from tesla import Tesla


def test_drive():
    tesla = Tesla("Model S", "Red")

    assert "Battery charge level is 99.9%" == tesla.drive(9000)
    assert "Battery charge level is 87.30000000000001%" == tesla.drive(42)


def test_lock_by_default():
    tesla = Tesla("Model S", "Red")

    assert "Car is locked!" == tesla.open_doors()
