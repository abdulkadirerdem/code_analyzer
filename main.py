import argparse
import json
import os
from core.scanner import find_python_files
from core.parser import parse_python_file
from core.graph_builder import build_dependency_graph
from core.analyzer import summarize_analysis
import networkx as nx


def run_analysis(path: str, target_file: str = None, output_format: str = "pretty"):
    print(f"🔍 Analyzing codebase at: {path}")
    
    if target_file:
        # Analyze a single file
        if not os.path.exists(target_file):
            print(f"Error: File {target_file} does not exist.")
            return
        
        print(f"📄 Analyzing Python file: {target_file}")
        file_data = {target_file: parse_python_file(target_file)}
        
        # Create a minimal graph
        graph = nx.DiGraph()
        graph.add_node(target_file)
    else:
        # Analyze all files in the directory
        files = find_python_files(path)
        print(f"📄 Found {len(files)} Python files.")
        
        file_data = {f: parse_python_file(f) for f in files}
        
        print("🔗 Building dependency graph...")
        graph = build_dependency_graph(file_data)

    print("🧠 Running static analysis...")
    result = summarize_analysis(graph, file_data)

    # Filter for target file if specified
    if target_file and target_file.endswith('.py'):
        base_name = os.path.basename(target_file)
        if base_name in result:
            result = {base_name: result[base_name]}
        else:
            print(f"Warning: No analysis available for {base_name}")
            return

    print("\n📊 Analysis Report:\n")
    if output_format == "json":
        # The result is already in the requested format
        formatted_output = json.dumps(result, indent=2, ensure_ascii=False)
        print(formatted_output)
    else:
        # Pretty print, keeping the desired format
        for file_path, file_info in result.items():
            print(f"File: {file_info['file']}")
            print("Functions:")
            for func in file_info["functions"]:
                print(f"  - {func['name']}")
                print(f"    Docstring: {func['docstring']}")
                print(f"    Fan-in: {func['fan_in']}, Fan-out: {func['fan_out']}")
                print(f"    Entry Point: {func['is_entry_point']}")
                print(f"    Code:\n{func['code']}")
                print("")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python Codebase Analyzer")
    parser.add_argument(
        "--path",
        type=str,
        default="tests/mock_project",
        help="Project directory to analyze",
    )
    parser.add_argument(
        "--file",
        type=str,
        help="Analyze only this specific Python file",
    )
    parser.add_argument("--json", action="store_true", help="Output results as JSON")

    args = parser.parse_args()
    run_analysis(args.path, args.file, output_format="json" if args.json else "pretty")
