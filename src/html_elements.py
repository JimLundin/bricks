"""Defining standard html elements."""

from __future__ import annotations

from typing import Self

from src.element import Attribute, Content, Element


class Head(Element):
    """Represents the head of an HTML document."""

    def __init__(
        self: Self,
        *content: Content,
        **attribute: Attribute,
    ) -> None:
        """Element with the name "head" and the content and attributes."""
        super().__init__("head", *content, **attribute)


class Body(Element):
    """Represents the body of an HTML document."""

    def __init__(
        self: Self,
        *content: Content,
        **attribute: Attribute,
    ) -> None:
        """Element with the name "body" and the content and attributes."""
        super().__init__("body", *content, **attribute)


class Html(Element):
    """Represents the root element of an HTML document."""

    def __init__(
        self: Self,
        head: Head | None = None,
        body: Body | None = None,
        *content: Content,
        **attribute: Attribute,
    ) -> None:
        """Element with the name "html" and the content and attributes."""
        head = head or Head()
        body = body or Body(*content)

        super().__init__("html", *(head, body), **attribute)

    def __str__(self: Self) -> str:
        """Convert the element to a string."""
        return f"<!DOCTYPE html>{super().__str__()}"


class Div(Element):
    """Element representing a <div> tag."""

    def __init__(
        self: Self,
        *content: Content,
        **attribute: Attribute,
    ) -> None:
        """Element with the name "div" and the content and attributes."""
        super().__init__("div", *content, **attribute)


class P(Element):
    """Element representing a <p> tag."""

    def __init__(
        self: Self,
        *content: Content,
        **attribute: Attribute,
    ) -> None:
        """Element with the name "p" and the content and attributes."""
        super().__init__("p", *content, **attribute)


class A(Element):
    """Element representing an <a> tag."""

    def __init__(
        self: Self,
        *content: Content,
        **attribute: Attribute,
    ) -> None:
        """Element with the name "a" and the content and attributes."""
        super().__init__("a", *content, **attribute)


class H1(Element):
    """Element representing an <h1> tag."""

    def __init__(
        self: Self,
        *content: Content,
        **attribute: Attribute,
    ) -> None:
        """Element with the name "h1" and the content and attributes."""
        super().__init__("h1", *content, **attribute)
