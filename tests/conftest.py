"""conftest file."""

import tempfile
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def workspace() -> Path:
    """Create a workspace for the test session."""
    return Path(tempfile.mkdtemp())
