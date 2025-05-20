import pytest
from asteroids.api import get_asteroids

from asteroids.api import get_asteroids

def test_get_asteroids_returns_dict():
    result = get_asteroids("2025-01-29")

    assert isinstance(result, dict)
    assert "asteroid" in result

    asteroid = result["asteroid"]
    assert "name" in asteroid
    assert "distance_km" in asteroid
