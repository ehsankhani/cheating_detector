import os
import ast
import pandas as pd
from algorithms.ast_comparator import ASTComparator
from algorithms.tokenizer import EnhancedTokenizer
from algorithms.levenshtein import similarity_score as levenshtein_similarity


# New feature extraction functions
def code_length(code):
    """Returns the number of lines in the code."""
    return len(code.splitlines())


def function_count(code):
    """Returns the number of function definitions in the code."""
    return code.count('def ')


def variable_count(code):
    """Returns the number of unique variable names in the code."""
    tokens = [token for token in code.split() if token.isidentifier()]
    return len(set(tokens))


def comment_ratio(code):
    """Returns the ratio of commented lines to total lines."""
    lines = code.splitlines()
    comment_lines = sum(1 for line in lines if line.strip().startswith('#'))
    return comment_lines / len(lines) if lines else 0


def cyclomatic_complexity(code):
    """Calculates cyclomatic complexity of the code using the AST module."""
    # Parse the code into an Abstract Syntax Tree (AST)
    tree = ast.parse(code)
    complexity = 1  # Start with one for the method itself

    # Visitor class to count control flow constructs
    class ControlFlowVisitor(ast.NodeVisitor):
        def visit_If(self, node):
            nonlocal complexity
            complexity += 1
            self.generic_visit(node)

        def visit_For(self, node):
            nonlocal complexity
            complexity += 1
            self.generic_visit(node)

        def visit_While(self, node):
            nonlocal complexity
            complexity += 1
            self.generic_visit(node)

        def visit_Try(self, node):
            nonlocal complexity
            complexity += 1
            self.generic_visit(node)

        def visit_With(self, node):
            nonlocal complexity
            complexity += 1
            self.generic_visit(node)

        def visit_ExceptHandler(self, node):
            nonlocal complexity
            complexity += 1

    # Traverse the AST
    ControlFlowVisitor().visit(tree)
    return complexity


# Set up directories
current_dir = os.getcwd()
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
grandparent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))

# Define directories
code_dir = os.path.join(grandparent_dir, 'DataSet')
csv_file = os.path.join(grandparent_dir, 'DataSet', 'cheating_dataset.csv')

# Initialize feature extractors
ast_comparator = ASTComparator()
tokenizer = EnhancedTokenizer()


def extract_features(file1, file2):
    # Read file contents
    with open(os.path.join(code_dir, file1), 'r') as f:
        code1 = f.read()
    with open(os.path.join(code_dir, file2), 'r') as f:
        code2 = f.read()

    # Compute features
    ast_sim = ast_comparator.compare_functions(code1, code2)
    token_sim = tokenizer.compare_tokens(code1, code2)
    lev_sim = levenshtein_similarity(code1, code2)

    # New features
    length1 = code_length(code1)
    length2 = code_length(code2)
    func_count1 = function_count(code1)
    func_count2 = function_count(code2)
    var_count1 = variable_count(code1)
    var_count2 = variable_count(code2)
    comment_ratio1 = comment_ratio(code1)
    comment_ratio2 = comment_ratio(code2)
    cyclomatic1 = cyclomatic_complexity(code1)
    cyclomatic2 = cyclomatic_complexity(code2)

    return (ast_sim, token_sim, lev_sim,
            length1, length2,
            func_count1, func_count2,
            var_count1, var_count2,
            comment_ratio1, comment_ratio2,
            cyclomatic1, cyclomatic2)


# Load CSV and remove whitespace from column names
csv_data = pd.read_csv(csv_file)
csv_data.columns = csv_data.columns.str.strip()  # Ensure no leading/trailing whitespace

# Create DataFrame for features
features_list = []
for index, row in csv_data.iterrows():
    file1 = row['File_1']  # Use the correct column name
    file2 = row['File_2']  # Use the correct column name
    extracted_features = extract_features(file1, file2)
    features_list.append(extracted_features + (row['Label'],))

# Create DataFrame
features_df = pd.DataFrame(features_list, columns=[
    'AST Similarity',
    'Token Similarity',
    'Levenshtein Similarity',
    'Length File 1',
    'Length File 2',
    'Function Count File 1',
    'Function Count File 2',
    'Variable Count File 1',
    'Variable Count File 2',
    'Comment Ratio File 1',
    'Comment Ratio File 2',
    'Cyclomatic Complexity File 1',
    'Cyclomatic Complexity File 2',
    'Label'
])

# Save the new dataset with features
csv_filename = os.path.join(grandparent_dir, "DataSet", "cheating_features_dataset.csv")
features_df.to_csv(csv_filename, index=False)

print(f"Saved to: {csv_filename}")
