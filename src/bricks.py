"""Serves the basic HTML generation for the package."""

from typing import Self

AttributeType = str | int | bool


class Element:
    """Defines the basid structure of an HTML element."""

    def __init__(
        self: Self,
        name: str,
        *content: str | Self,
        **attribute: AttributeType,
    ) -> None:
        """HTML element with mandatory name, and optional content and attributes."""
        self.name = name
        self.content = content
        self.attribute = attribute

    def __call__(self: Self, *content: str | Self, **attribute: AttributeType) -> Self:
        """Create a new element with the same name and attributes."""
        if content:
            self.content += content
        if attribute:
            self.attribute.update(attribute)
        return self

    def __str__(self: Self) -> str:
        """Convert the element to a string."""

        def format_attribute(key: str, value: AttributeType) -> str:
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
