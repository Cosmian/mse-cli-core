"""conftest file."""

import tempfile
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def workspace(tmp_path_factory) -> Path:
    """Create a workspace for the test session."""
    return tmp_path_factory.mktemp("workspace")
