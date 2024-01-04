"""Tests for the element function."""

import pytest

from src.bricks import Element


@pytest.fixture()
def div_without_attrs() -> Element:
    return Element("div")("test")


@pytest.fixture()
def div_with_attrs() -> Element:
    return Element("div")(style="test")("test")


def test_element_without_attrs(div_without_attrs: Element) -> None:
    assert str(div_without_attrs) == "<div>test</div>"


def test_element_with_attrs(div_with_attrs: Element) -> None:
    assert str(div_with_attrs) == '<div style="test">test</div>'


def test_multiple_attributes_and_content() -> None:
    element = Element("p")(class_="paragraph", id="my-id")("This is a paragraph.")
    assert str(element) == '<p class="paragraph" id="my-id">This is a paragraph.</p>'


def test_nested_elements() -> None:
    container = Element("div")(Element("p")("Paragraph 1"), Element("p")("Paragraph 2"))
    assert str(container) == "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>"


def test_empty_element() -> None:
    empty_element = Element("br")()
    assert str(empty_element) == "<br>"
