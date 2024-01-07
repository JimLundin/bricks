from __future__ import annotations

from typing import Self

from src.bricks import Attribute, Element


class Div(Element):
    """Element representing a <div> tag."""

    def __init__(
        self: Self,
        *content: Attribute | Element,
        **attribute: Attribute,
    ) -> None:
        """Element with the name "div" and the content and attributes."""
        super().__init__("div", *content, **attribute)


class P(Element):
    """Element representing a <p> tag."""

    def __init__(
        self: Self,
        *content: Attribute | Element,
        **attribute: Attribute,
    ) -> None:
        """Element with the name "p" and the content and attributes."""
        super().__init__("p", *content, **attribute)


class A(Element):
    """Element representing an <a> tag."""

    def __init__(
        self: Self,
        *content: Attribute | Element,
        **attribute: Attribute,
    ) -> None:
        """Element with the name "a" and the content and attributes."""
        super().__init__("a", *content, **attribute)


class H1(Element):
    """Element representing an <h1> tag."""

    def __init__(
        self: Self,
        *content: Attribute | Element,
        **attribute: Attribute,
    ) -> None:
        """Element with the name "h1" and the content and attributes."""
        super().__init__("h1", *content, **attribute)
