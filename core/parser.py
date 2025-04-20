import ast


def parse_python_file(filepath: str) -> dict:
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)

    imports = []
    imported_symbols = []
    exports = []
    dynamic_imports = []
    aliases = {}

    for node in ast.walk(tree):
        # Static imports: import x or from x import y
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
                aliases[alias.asname or alias.name] = alias.name

        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)
            for alias in node.names:
                imported_symbols.append(alias.name)
                aliases[alias.asname or alias.name] = alias.name

        # Exports: functions, classes, constants
        elif isinstance(node, ast.FunctionDef):
            exports.append(node.name)

        elif isinstance(node, ast.ClassDef):
            exports.append(node.name)

        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    exports.append(target.id)

        # Dynamic imports
        elif isinstance(node, ast.Call):
            func_name = getattr(node.func, "id", "")
            if func_name in ("__import__", "import_module"):
                dynamic_imports.append(ast.unparse(node))

    return {
        "file": filepath,
        "imports": list(set(imports)),
        "imported_symbols": list(set(imported_symbols)),
        "exports": list(set(exports)),
        "dynamic_imports": dynamic_imports,
        "aliases": aliases,
    }
