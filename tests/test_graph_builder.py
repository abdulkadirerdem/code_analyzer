from core.graph_builder import build_dependency_graph
from core.parser import parse_python_file
from core.scanner import find_python_files


def test_graph_builder():
    files = find_python_files("tests/mock_project")
    file_data = {f: parse_python_file(f) for f in files}

    graph = build_dependency_graph(file_data)

    assert graph.number_of_nodes() == len(files)
    assert isinstance(graph.edges, object)
    print("Edges:", list(graph.edges))
