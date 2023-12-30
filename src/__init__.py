"""Serves the basic HTML generation for the package."""

from typing import Self

from elements import standard_elements

AttributeType = str | int | bool | None


class Tag:
    """Represents the basic concept of an HTML tag."""

    def __init__(self: Self, name: str, **attributes: AttributeType) -> None:
        """Instatiates an HTML tag."""
        self.name = name
        self.attributes = attributes or {}

    def __call__(self: Self, *args: Self | str) -> Self:
        """Attach child elements and content when instance is called."""
        self.content = args
        return self

    def __str__(self: Self) -> str:
        """Create the string representation of the HTML element tree."""
        attribute_str = " ".join(
            [f'{key}="{value}"' for key, value in self.attributes.items()]
        )
        if self.content:
            opening_tag = f"<{self.name} {attribute_str}>"
            closing_tag = f"</{self.name}>"
            content_str = "".join([str(child) for child in self.content])
            return f"{opening_tag}{content_str}{closing_tag}"

        return f"<{self.name} {attribute_str} />"


# Dynamically create subclasses for standard HTML elements
for element in standard_elements:
    class_name = element.capitalize()
    setattr(
        Tag,
        class_name,
        type(
            class_name,
            (Tag,),
            {
                "__init__": lambda self, attributes=None: super().__init__(
                    element, attributes
                )
            },
        ),
    )

# Example usage:
if __name__ == "__main__":
    # Use the provided syntax for creating nested elements
    html_structure = Div(class_name="container")(P()("Hello, ", Span()("World!")))

    h1_element = H1(attributes={"style": "color: blue;"})("Heading 1")

    # Generate and print the HTML
    generated_html = "".join([str(element) for element in [html_structure, h1_element]])
    print(generated_html)
