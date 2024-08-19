from ast_comparator import ASTComparator


class BlockPermutationDetector:
    def __init__(self):
        self.ast_comparator = ASTComparator()

    def permutation_similarity(self, code1, code2):
        blocks1 = sorted(self.ast_comparator.extract_functions(code1))
        blocks2 = sorted(self.ast_comparator.extract_functions(code2))

        # Direct comparison after sorting
        common_blocks = set(blocks1).intersection(set(blocks2))
        similarity = len(common_blocks) / max(len(blocks1), len(blocks2), 1)
        return similarity
