import pytest
import myfactorial

def test_myfactorial():
    assert myfactorial.factorial(3) == 6
    assert myfactorial.factorial(0) == 1
    assert type(myfactorial.factorial(-2)) == int

