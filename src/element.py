"""Serves the basic HTML generation for the package."""
from __future__ import annotations

from typing import Self, Union

Attribute = str | int | bool
Content = Union[Attribute, "Element"]


class Element:
    """Defines the basic structure of an HTML element."""

    def __init__(
        self: Self,
        name: str,
        *content: Content,
        **attribute: Attribute,
    ) -> None:
        """HTML element with mandatory name, and optional content and attributes."""
        self.name = name
        self.content = content
        self.attribute = attribute

    def __call__(
        self: Self,
        *content: Content,
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
