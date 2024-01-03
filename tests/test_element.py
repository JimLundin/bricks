"""Tests for the element function."""

from bricks import element


def test_element() -> None:
    div = element("div")("test")
    assert div == "<div>test</div>"
