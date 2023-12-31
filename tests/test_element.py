"""Tests for the element function."""


from src.element import Element
from src.html_elements import H1, A, Div, P


def test_element_without_attrs() -> None:
    element = Element("div")("test")
    assert str(element) == "<div>test</div>"


def test_element_with_attrs() -> None:
    element = Element("div")(style="test")("test")
    assert str(element) == '<div style="test">test</div>'


def test_multiple_attributes_and_content() -> None:
    element = Element("p")(class_="paragraph", id="my-id")("This is a paragraph.")
    assert str(element) == '<p class="paragraph" id="my-id">This is a paragraph.</p>'


def test_nested_elements() -> None:
    container = Element("div")(Element("p")("Paragraph 1"), Element("p")("Paragraph 2"))
    assert str(container) == "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>"


def test_empty_element() -> None:
    empty_element = Element("br")
    assert str(empty_element) == "<br>"


def test_element_with_attrs_underscore() -> None:
    element = Element("div")(style="test", data_value="123")("test")
    assert str(element) == '<div style="test" data-value="123">test</div>'


def test_attribute_formatting() -> None:
    element = Element("a")(href="https://example.com", aria_label="Link")("Click me")
    assert (
        str(element) == '<a href="https://example.com" aria-label="Link">Click me</a>'
    )


def test_reserved_keyword_in_attribute_name() -> None:
    element = Element("span")(class_="highlight")("Text")
    assert str(element) == '<span class="highlight">Text</span>'


def test_multiple_attributes_and_content_with_formatting() -> None:
    element = Element("button")(type_="button", disabled=True, custom_data_value="123")(
        "Click me",
    )
    assert (
        str(element)
        == '<button type="button" disabled custom-data-value="123">Click me</button>'
    )


def test_attribute_with_underscore() -> None:
    element = Element("input")(type_="text", placeholder="Enter text")
    assert str(element) == '<input type="text" placeholder="Enter text">'


def test_nested_elements_with_strings() -> None:
    element = Element("div")(
        Element("p")("Paragraph 1"),
        Element("span", class_="highlight")("Nested Span"),
        '<a href="https://example.com">Link</a>',
        Element("div")(Element("strong")("Nested Strong")),
    )
    expected_result = (
        "<div>"
        "<p>Paragraph 1</p>"
        '<span class="highlight">Nested Span</span>'
        '<a href="https://example.com">Link</a>'
        "<div><strong>Nested Strong</strong></div>"
        "</div>"
    )
    assert str(element) == expected_result


def test_nested_elements_with_f_string() -> None:
    element = Element("div")(
        "<p>Paragraph 1</p>",
        Element("span")("Nested Span"),
        '<a href="https://example.com">Link</a>',
        "<div><strong>Nested Strong</strong></div>",
    )
    expected_result = (
        "<div>"
        "<p>Paragraph 1</p>"
        "<span>Nested Span</span>"
        '<a href="https://example.com">Link</a>'
        "<div><strong>Nested Strong</strong></div>"
        "</div>"
    )
    assert str(element) == expected_result


def test_nested_elements_with_f_strings() -> None:
    element = Element("div")(
        "<p>Paragraph 1</p>",
        f'Embedded Element: {Element("span")("Nested Span")}',
        '<a href="https://example.com">Link</a>',
        "<div><strong>Nested Strong</strong></div>",
    )
    expected_result = (
        "<div>"
        "<p>Paragraph 1</p>"
        "Embedded Element: <span>Nested Span</span>"
        '<a href="https://example.com">Link</a>'
        "<div><strong>Nested Strong</strong></div>"
        "</div>"
    )
    assert str(element) == expected_result


def test_div() -> None:
    div_element = Div(style="background-color: #eee")("This is a standard div")
    assert (
        str(div_element)
        == '<div style="background-color: #eee">This is a standard div</div>'
    )


def test_p() -> None:
    p_element = P(class_="paragraph")("This is a standard paragraph")
    assert str(p_element) == '<p class="paragraph">This is a standard paragraph</p>'


def test_a() -> None:
    a_element = A(href="https://example.com")("Visit Example")
    assert str(a_element) == '<a href="https://example.com">Visit Example</a>'


def test_h1() -> None:
    h1_element = H1()("Heading 1")
    assert str(h1_element) == "<h1>Heading 1</h1>"


def test_nested_subclass_elements() -> None:
    h1_inside_div = Div(H1("Heading 1"))
    assert str(h1_inside_div) == "<div><h1>Heading 1</h1></div>"
