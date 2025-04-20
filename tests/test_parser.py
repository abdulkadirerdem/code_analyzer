from core.parser import parse_python_file


def test_parse_python_file():
    result = parse_python_file("tests/mock_project/a.py")

    assert isinstance(result["imports"], list)
    assert isinstance(result["exports"], list)
    assert "a" in result["exports"]

    print("\n\nParsed:", result)
