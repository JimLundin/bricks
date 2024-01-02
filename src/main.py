from collections.abc import Iterable
from html import escape
from typing import Self

RenderTag = str | int | Frag | None | Iterable["RenderTag"]


def render(tag: RenderTag, builder: list[str]) -> None:
    match tag:
        case None:
            return
        case str():
            builder.append(escape(tag, quote=False))
        case Frag():
            tag.render_into(builder)
        case int():
            builder.append(str(tag))
        case Iterable():
            for element in tag:
                render_into(element, builder)


def render_tag(tag: RenderTag) -> str:
    builder: list[str] = []
    render_into(tag, builder)
    return "".join(builder)


Attribute = str | int | bool | Iterable[str | int | None] | dict[str, bool] | None


class Tag:
    def __init__(self: Self, name: str, **attrs: Attribute) -> None:
        # See "Tag name" in
        # https://www.w3.org/TR/html52/syntax.html#writing-html-documents-elements.
        if not (name and name.isascii() and name.isalnum()):
            msg = f"invalid html tag: {name}"
            raise ValueError(msg)
        self.name = name

        self.attrs = {_normalize_attr(attr): value for attr, value in attrs.items()}

    def render_into(self: Self, builder: list[str]) -> None:
        builder.append("<" + self.name)
        for attr, value in self.attrs.items():
            match value:
                case False | None | []:
                    continue
                case True:
                    value = ""
                case str():
                    pass
                case bytes():
                    msg = f"cannot render bytes as html attribute: {value!r}"
                    raise TypeError(msg)
                case Iterable():
                    if not value:
                        continue
                    value = " ".join(str(item) for item in value)
                case _:
                    value = str(value)

            # Attribute name is normalized/validated in constructor.
            builder.append(" " + attr)

            if not value:
                # If the value is an empty string, use empty attribute syntax.
                continue
            builder.append('="')
            builder.append(escape(value, quote=False).replace('"', "&quot;"))
            builder.append('"')
        builder.append(">")

    def __call__(self: Self, *children: RenderTag) -> _Tag:
        return _Tag(self, children)


class _Tag(Frag):
    def __init__(self: Self, tag: Tag, children: tuple[RenderTag, ...]) -> None:
        self.tag = tag
        self.children = children

    def render_into(self: Self, builder: list[str]) -> None:
        self.tag.render_into(builder)
        for child in self.children:
            render(child, builder)
        builder.append("</" + self.tag.name + ">")


class raw(Frag):
    def __init__(self: Self, html: str) -> None:
        self.html = html

    def render_into(self: Self, builder: list[str]) -> None:
        builder.append(self.html)


class frag(Frag):
    def __init__(self: Self, *children: RenderTag) -> None:
        self.children = children

    def render_into(self: Self, builder: list[str]) -> None:
        for child in self.children:
            render_into(child, builder)


class HTML(Tag):
    def __init__(self: Self, **attrs: Attribute) -> None:
        super().__init__("html", **attrs)

    def render_into(self: Self, builder: list[str]) -> None:
        builder.append("<!DOCTYPE html>")
        super().render_into(builder)


def _normalize_attr(attr: str) -> str:
    if attr in ["klass", "class_name"]:
        return "class"

    attr = attr.rstrip("_").replace("_", "-")

    # Slightly more restrictive than "Attribute names" in
    # https://www.w3.org/TR/html52/syntax.html#elements-attributes.
    if not (attr and attr.isascii()):
        msg = f"invalid html attribute name: {attr}"
        raise ValueError(msg)

    return attr
