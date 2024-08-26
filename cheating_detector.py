from file_reader import FileReader
from similarity_detector import SimilarityDetector
from ast_comparator import ASTComparator
from tokenizer import Tokenizer
from levenshtein import similarity_score as levenshtein_similarity


class CheatingDetector:
    def __init__(self, directory):
        self.reader = FileReader(directory)
        self.similarity_detector = None
        self.ast_comparator = ASTComparator()
        self.tokenizer = Tokenizer()
        self.levenshtein_similarity = levenshtein_similarity
        self.detailed_results = []  # Store detailed results here

    def analyze(self):
        files = self.reader.read_files()
        if not files:
            print("No files found for analysis.")
            return []

        self.similarity_detector = SimilarityDetector(files)
        results = self.similarity_detector.detect_similarities()

        enhanced_results = []
        for file1, file2, text_sim_score in results:
            # AST function hash comparison
            ast_sim_score = self.ast_comparator.compare_functions(files[file1], files[file2])

            # Token similarity
            token_sim_score = self.tokenizer.compare_tokens(files[file1], files[file2])

            # Levenshtein similarity
            lev_sim_score = self.levenshtein_similarity(files[file1], files[file2])

            # Weighted score calculation
            overall_score = (
                    0.2 * text_sim_score +
                    0.4 * ast_sim_score +  # Increased weight on AST similarity
                    0.2 * token_sim_score +
                    0.2 * lev_sim_score
            )

            if overall_score > 0.7:  # Adjust threshold as needed
                enhanced_results.append((file1, file2, overall_score))

        # Store the detailed results
        self.detailed_results = enhanced_results

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

    def get_detailed_results(self):
        """
        Return the detailed results after analysis.
        """
        if not self.detailed_results:
            print("No detailed results available. Run analyze() first.")
        return self.detailed_results
