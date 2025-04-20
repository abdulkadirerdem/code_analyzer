import networkx as nx


def detect_circular_imports(graph: nx.DiGraph) -> list[list[str]]:
    try:
        return list(nx.simple_cycles(graph))
    except Exception:
        return []


def calculate_fan_in_out(graph: nx.DiGraph) -> dict:
    return {
        node: {"fan_in": graph.in_degree(node), "fan_out": graph.out_degree(node)}
        for node in graph.nodes
    }


def find_dead_exports(file_data: dict) -> dict:
    all_code = ""
    for fpath in file_data:
        with open(fpath, "r", encoding="utf-8") as f:
            all_code += f.read()

    dead = {}
    for fpath, data in file_data.items():
        dead_symbols = []
        for symbol in data["exports"]:
            if all_code.count(symbol) <= 1:
                dead_symbols.append(symbol)
        if dead_symbols:
            dead[fpath] = dead_symbols

    return dead


def summarize_analysis(graph: nx.DiGraph, file_data: dict) -> dict:
    return {
        "circular_dependencies": detect_circular_imports(graph),
        "dead_code": find_dead_exports(file_data),
        "fan_analysis": calculate_fan_in_out(graph),
    }
