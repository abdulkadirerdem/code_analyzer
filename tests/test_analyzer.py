from core.analyzer import summarize_analysis
from core.parser import parse_python_file
from core.scanner import find_python_files
from core.graph_builder import build_dependency_graph


def test_summarize_analysis():
    files = find_python_files("tests/mock_project")
    file_data = {f: parse_python_file(f) for f in files}
    graph = build_dependency_graph(file_data)

    analysis = summarize_analysis(graph, file_data)

    print("\n\n🔁 Circular:", analysis["circular_dependencies"])
    print("\n💀 Dead code:", analysis["dead_code"])
    print("\n📊 Fan In/Out:", analysis["fan_analysis"])

    assert isinstance(analysis, dict)
