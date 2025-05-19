import pytest
from asteroids.api import get_asteroids

from asteroids.api import get_asteroids

def test_get_asteroids_returns_dict():
    # Call the real function with a real date (limited usage with DEMO_KEY)
    result = get_asteroids("2025-01-29")

    # Check that it returns a dictionary with an "asteroid" key
    assert isinstance(result, dict)
    assert "asteroid" in result

    asteroid = result["asteroid"]
    assert "name" in asteroid
    assert "distance_km" in asteroid
