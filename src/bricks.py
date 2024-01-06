"""Serves the basic HTML generation for the package."""
from __future__ import annotations

from typing import Self

from src.elements import STANDARD_ELEMENTS

Attribute = str | int | bool


class Element:
    """Defines the basic structure of an HTML element."""

    def __init__(
        self: Self,
        name: str,
        *content: Attribute | Element,
        **attribute: Attribute,
    ) -> None:
        """HTML element with mandatory name, and optional content and attributes."""
        self.name = name
        self.content = content
        self.attribute = attribute

    def __call__(
        self: Self,
        *content: Attribute | Element,
        **attribute: Attribute,
    ) -> Self:
        """Create a new element with the same name and attributes."""
        if content:
            self.content += content
        if attribute:
            self.attribute.update(attribute)
        return self

    def __str__(self: Self) -> str:
        """Convert the element to a string."""

        def format_attribute(key: str, value: Attribute) -> str:
            formatted_key = key.rstrip("_").replace("_", "-")
            if isinstance(value, bool):
                if value:
                    return f" {formatted_key}"
                return ""
            return f' {formatted_key}="{value}"'

        attribute = "".join(
            format_attribute(key, value) for key, value in self.attribute.items()
        )

        opening_tag = f"<{self.name}{attribute}>"
        content = "".join(str(item) for item in self.content)
        closing_tag = f"</{self.name}>" if self.content else ""

        return f"{opening_tag}{content}{closing_tag}"


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


def create_standard_element_class(element_name: str) -> type[Element]:
    """Create a class that inherits from Element and adds the name."""

    class StandardElement(Element):
        def __init__(
            self: Self,
            *content: Attribute | Element,
            **attribute: Attribute,
        ) -> None:
            super().__init__(element_name, *content, **attribute)

    StandardElement.__name__ = element_name

    return StandardElement


for standard_element in STANDARD_ELEMENTS:
    StandardElement = create_standard_element_class(standard_element)
    globals()[standard_element] = StandardElement
