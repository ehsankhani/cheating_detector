import re
from radon.complexity import cc_visit


def count_functions_and_variables(code):
    function_pattern = re.compile(r'\bdef\b')
    variable_pattern = re.compile(r'\b\w+\s*=\s*')

    function_count = len(function_pattern.findall(code))
    variable_count = len(variable_pattern.findall(code))

    return function_count, variable_count


def calculate_comment_ratio(code):
    total_lines = len(code.splitlines())
    comment_lines = sum(1 for line in code.splitlines() if line.strip().startswith('#'))

    if total_lines == 0:
        return 0
    return comment_lines / total_lines


def calculate_cyclomatic_complexity_average(code):
    blocks = cc_visit(code)
    if not blocks:
        return 0
    return sum(block.complexity for block in blocks) / len(blocks)


def extract_extra_features(code1, code2):
    # Function count and variable count
    function_count1, variable_count1 = count_functions_and_variables(code1)
    function_count2, variable_count2 = count_functions_and_variables(code2)

    # Comment ratio
    comment_ratio1 = calculate_comment_ratio(code1)
    comment_ratio2 = calculate_comment_ratio(code2)

    # Cyclomatic complexity
    cyclomatic_complexity1 = calculate_cyclomatic_complexity_average(code1)
    cyclomatic_complexity2 = calculate_cyclomatic_complexity_average(code2)

    return {
        'Function Count File 1': function_count1,
        'Function Count File 2': function_count2,
        'Variable Count File 1': variable_count1,
        'Variable Count File 2': variable_count2,
        'Comment Ratio File 1': comment_ratio1,
        'Comment Ratio File 2': comment_ratio2,
        'Cyclomatic Complexity File 1': cyclomatic_complexity1,
        'Cyclomatic Complexity File 2': cyclomatic_complexity2
    }
