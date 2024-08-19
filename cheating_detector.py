from file_reader import FileReader
from similarity_detector import SimilarityDetector
from ast_comparator import ASTComparator
from tokenizer import Tokenizer
from levenshtein import similarity_score as levenshtein_similarity
# from block_permutation_detector import BlockPermutationDetector


class CheatingDetector:
    def __init__(self, directory):
        self.reader = FileReader(directory)
        self.similarity_detector = None
        self.ast_comparator = ASTComparator()
        self.tokenizer = Tokenizer()
        self.levenshtein_similarity = levenshtein_similarity

    def analyze(self):
        files = self.reader.read_files()
        if not files:
            print("No files found for analysis.")
            return []

        self.similarity_detector = SimilarityDetector(files)
        results = self.similarity_detector.detect_similarities()

        enhanced_results = []
        for file1, file2, text_sim_score in results:
            # AST similarity
            ast_sim_score = self.ast_comparator.compare_functions(files[file1], files[file2])

            # Token similarity
            token_sim_score = self.tokenizer.compare_tokens(files[file1], files[file2])

            # Levenshtein similarity
            lev_sim_score = self.levenshtein_similarity(files[file1], files[file2])

            # Weighted score calculation
            overall_score = (
                    0.3 * text_sim_score +
                    0.3 * ast_sim_score +  # Increased weight on AST similarity
                    0.2 * token_sim_score +
                    0.2 * lev_sim_score
            )

            if overall_score > 0.85:  # Adjust threshold as needed
                enhanced_results.append((file1, file2, overall_score))

        return enhanced_results

    def get_cheating_report(self):
        results = self.analyze()
        if not results:
            print("No potential cheating detected.")
            return ["No potential cheating detected."]

        report = []
        for file1, file2, score in results:
            report.append(f'Possible cheating between {file1} and {file2} with a similarity score of {score:.2f}')
        return report
