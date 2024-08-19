import itertools
from ast_comparator import ASTComparator


class BlockPermutationDetector:
    def __init__(self):
        self.ast_comparator = ASTComparator()

    def permutation_similarity(self, code1, code2):
        blocks1 = self.ast_comparator.extract_functions(code1)
        blocks2 = self.ast_comparator.extract_functions(code2)

        max_similarity = 0
        for perm in itertools.permutations(blocks2):
            common_blocks = set(blocks1).intersection(set(perm))
            similarity = len(common_blocks) / max(len(blocks1), len(blocks2), 1)
            if similarity > max_similarity:
                max_similarity = similarity

        return max_similarity
