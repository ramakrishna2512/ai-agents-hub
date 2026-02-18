import ast

def validate_test_cases(code, expected_count):
    try:
        tree = ast.parse(code)

        test_functions = [
            node for node in tree.body
            if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
        ]

        if len(test_functions) == expected_count:
            return True
        else:
            return False

    except:
        return False
