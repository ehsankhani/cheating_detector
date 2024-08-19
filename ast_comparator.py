import ast
import astunparse


class ASTComparator:
    def normalize_ast(self, code):
        tree = ast.parse(code)
        normalized_tree = self._normalize_tree(tree)
        return astunparse.unparse(normalized_tree)

    def _normalize_tree(self, node):
        for child in ast.iter_child_nodes(node):
            if isinstance(child, ast.Name):
                child.id = "_var"
            elif isinstance(child, ast.FunctionDef):
                child.name = "_func"
            self._normalize_tree(child)
        return node

    def compare_ast(self, code1, code2):
        normalized_code1 = self.normalize_ast(code1)
        normalized_code2 = self.normalize_ast(code2)
        return normalized_code1 == normalized_code2

    def similarity_score(self, code1, code2):
        return self.compare_ast(code1, code2)

    def extract_functions(self, code):
        tree = ast.parse(code)
        functions = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append(ast.dump(self._normalize_tree(node)))
        return sorted(functions)  # Sort functions by their content

    def compare_functions(self, code1, code2):
        functions1 = self.extract_functions(code1)
        functions2 = self.extract_functions(code2)
        common_functions = set(functions1).intersection(set(functions2))
        return len(common_functions) / max(len(functions1), len(functions2), 1)
