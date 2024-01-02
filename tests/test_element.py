"""Tests for the element function."""

from src import element


def test_element() -> None:
    div = element("div")("test")
    assert div == "<div>test</div>"
