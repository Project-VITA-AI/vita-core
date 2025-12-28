"""Pytest configuration and fixtures."""
import pytest


@pytest.fixture
def example_fixture():
    """Example fixture for tests."""
    return {"example": "data"}

