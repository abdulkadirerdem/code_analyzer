import argparse
import json
from core.scanner import find_python_files
from core.parser import parse_python_file
from core.graph_builder import build_dependency_graph
from core.analyzer import summarize_analysis
from pprint import pprint


def run_analysis(path: str, output_format: str = "pretty"):
    print(f"🔍 Analyzing codebase at: {path}")
    files = find_python_files(path)

    print(f"📄 Found {len(files)} Python files.")
    file_data = {f: parse_python_file(f) for f in files}

    print("🔗 Building dependency graph...")
    graph = build_dependency_graph(file_data)

    print("🧠 Running static analysis...")
    result = summarize_analysis(graph, file_data)

    print("\n📊 Analysis Report:\n")
    if output_format == "json":
        print(json.dumps(result, indent=2))
    else:
        pprint(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python Codebase Analyzer")
    parser.add_argument(
        "--path",
        type=str,
        default="tests/mock_project",
        help="Project directory to analyze",
    )
    parser.add_argument("--json", action="store_true", help="Output results as JSON")

    args = parser.parse_args()
    run_analysis(args.path, output_format="json" if args.json else "pretty")
