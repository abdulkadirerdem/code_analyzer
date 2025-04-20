from core.scanner import find_python_files


def test_find_python_files():
    result = find_python_files("tests/mock_project")
    assert any("a.py" in f for f in result)
