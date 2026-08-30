"""Shared pytest fixtures."""

import os

import pytest
from app.app import app, csrf


@pytest.fixture
def client():
    """Set up Flask client for use in tests."""
    app.secret_key = os.urandom(12).hex()
    csrf.init_app(app)
    web_client = app.test_client()
    yield web_client
