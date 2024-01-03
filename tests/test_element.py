"""Tests for the element function."""

from src.bricks import Element


def test_basic_element() -> None:
    div = Element("div")("test")
    assert div == "<div>test</div>"


def test_element_with_id() -> None:
    div = Element("div")(id="test")("test")
    assert div == '<div id="test">test</div>'
