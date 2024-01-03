"""Serves the basic HTML generation for the package."""

from typing import Self


class Element:
    """Defines the basid structure of an HTML element."""

    def __init__(self: Self, name: str, *content: str | Self, **attribute: str) -> None:
        """HTML element with mandatory name, and optional content and attributes."""
        self.name = name
        self.content = content
        self.attribute = attribute

    def __call__(self: Self, *content: str | Self, **attribute: str) -> Self:
        """Create a new element with the same name and attributes."""
        if content:
            self.content += content
        if attribute:
            self.attribute.update(attribute)
        return self

    def __str__(self: Self) -> str:
        """Convert the element to a string."""
        attribute = " ".join(
            f' {key}="{value}"' for key, value in self.attribute.items()
        )
        content = "".join(str(item) for item in self.content)

        return f"<{self.name}{attribute}>{content}</{self.name}>"
