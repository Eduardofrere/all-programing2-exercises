from prime import is_prime
import pytest

def test_known_primes():
    assert is_prime(2) == (2, "is prime")
    assert is_prime(13) == (13, "is prime")

def test_known_non_primes():
    assert is_prime(1) == (1, "is not prime")
    assert is_prime(14) == (14, "is not prime")
    assert is_prime(-7) == (-7, "is not prime")
    
def test_not_integers():
    with pytest.raises(ValueError):
        is_prime(32.47)
    
def test_strings():
    with pytest.raises(ValueError):
        is_prime("hello")

def test_convertible_Strings():
    assert is_prime("7") == (7, "is prime")






