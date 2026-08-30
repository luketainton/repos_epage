"""Tests for the Flask application."""


def test_index(client) -> None:
    """Ensure the index page is loaded correctly."""
    req = client.get("/")
    assert req.status_code == 200 and "ePage" in req.text
