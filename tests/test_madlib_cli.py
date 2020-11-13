from madlib_cli import __version__
from madlib_cli.madlib_cli import read_template, parse_template, merge

def test_version():
    assert __version__ == '0.1.0'

def test_read_template_returns_stripped_string():
    actual = read_template("./assets/easy_peasy.txt")
    expected = "Make Me A Video Game!\n\nI the {Adjective} and {Adjective} {Noun}."
    assert actual == expected

def test_parse_template():
    actual_stripped, actual_parts = parse_template("Make Me A Video Game!\n\nI the {Adjective} and {Adjective} {Noun}.")
    expected_stripped = "Make Me A Video Game!\n\nI the {} and {} {}."
    expected_parts = ["Adjective", "Adjective", "Noun"]

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts

def test_merge():
    actual = merge("Make Me A Video Game!\n\nI the {} and {} {}.", ["dark", "stormy", "night"])
    expected = "Make Me A Video Game!\n\nI the dark and stormy night."
    assert actual == expected