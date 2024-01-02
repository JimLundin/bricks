"""Serves the basic HTML generation for the package."""

__all__ = ["element"]

from collections.abc import Callable, Iterable

Attribute = str | int | bool | None


def element(name: str) -> Callable[..., str | Callable[..., str]]:
    """Generate a generic HTML tag, possibly via currying."""

    def named_element(
        *contents: str, **attributes: Attribute,
    ) -> str | Callable[..., str]:
        def render_element(contents: Iterable[str]) -> str:
            if attributes:
                attribute = " ".join(
                    [
                        f'{key.replace("_", "-")}="{value}"'
                        for key, value in attributes.items()
                    ],
                )

            body = "".join(contents)

            tag_open = f"<{name} {attribute}>" if attribute else f"<{name}>"

            tag_close = f"</{name}>"

            return f"{tag_open}{body}{tag_close}"

        if contents:
            return render_element(contents)

        return render_element

    return named_element
