import ast
import astunparse
import hashlib


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

    def hash_function(self, func_node):
        """
        Generates a hash for a given function node.
        """
        function_ast_dump = ast.dump(func_node, annotate_fields=False)
        return hashlib.md5(function_ast_dump.encode()).hexdigest()

    def extract_function_hashes(self, code):
        """
        Extracts and returns a sorted list of hashes for all functions in the code.
        """
        tree = ast.parse(code)
        function_hashes = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_hash = self.hash_function(node)
                function_hashes.append(func_hash)

        return sorted(function_hashes)

    def compare_functions(self, code1, code2):
        """
        Compares the function hashes between two pieces of code.
        """
        hashes1 = self.extract_function_hashes(code1)
        hashes2 = self.extract_function_hashes(code2)

        if len(hashes1) == 0 or len(hashes2) == 0:
            return 0

        common_hashes = set(hashes1).intersection(set(hashes2))
        return len(common_hashes) / max(len(hashes1), len(hashes2))