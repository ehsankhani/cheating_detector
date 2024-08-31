import os
import joblib
import pandas as pd
from Utils.file_reader import FileReader
from algorithms.similarity_detector import SimilarityDetector
from algorithms.ast_comparator import ASTComparator
from algorithms.tokenizer import Tokenizer
from algorithms.levenshtein import similarity_score as levenshtein_similarity
from algorithms.extra_features import extract_extra_features  # Import the new module


class CheatingDetector:
    def __init__(self, directory):
        self.reader = FileReader(directory)
        self.similarity_detector = None
        self.ast_comparator = ASTComparator()
        self.tokenizer = Tokenizer()
        self.levenshtein_similarity = levenshtein_similarity
        self.detailed_results = []

        # Load the machine learning model and scaler
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.model = joblib.load(os.path.join(current_dir, 'ML', 'cheating_detector_model.pkl'))
        self.scaler = joblib.load(os.path.join(current_dir, 'ML', 'scaler.pkl'))

    def analyze(self):
        try:
            files = self.reader.read_files()
            if not files:
                print("No files found for analysis.")
                return []

            self.similarity_detector = SimilarityDetector(files)
            results = self.similarity_detector.detect_similarities()

            enhanced_results = []
            for file1, file2, text_sim_score in results:
                # Debug output
                print(f"Comparing {file1} and {file2}")

                ast_sim_score = self.ast_comparator.compare_functions(files[file1], files[file2])
                token_sim_score = self.tokenizer.compare_tokens(files[file1], files[file2])
                lev_sim_score = self.levenshtein_similarity(files[file1], files[file2])

                # Extract additional features
                extra_features = extract_extra_features(files[file1], files[file2])

                # Combine all features into a DataFrame
                features_df = pd.DataFrame({
                    'AST Similarity': [ast_sim_score],
                    'Token Similarity': [token_sim_score],
                    'Levenshtein Similarity': [lev_sim_score],
                    'Length File 1': [len(files[file1])],
                    'Length File 2': [len(files[file2])],
                    'Function Count File 1': [extra_features['Function Count File 1']],
                    'Function Count File 2': [extra_features['Function Count File 2']],
                    'Variable Count File 1': [extra_features['Variable Count File 1']],
                    'Variable Count File 2': [extra_features['Variable Count File 2']],
                    'Comment Ratio File 1': [extra_features['Comment Ratio File 1']],
                    'Comment Ratio File 2': [extra_features['Comment Ratio File 2']],
                    'Cyclomatic Complexity File 1': [extra_features['Cyclomatic Complexity File 1']],
                    'Cyclomatic Complexity File 2': [extra_features['Cyclomatic Complexity File 2']]
                })

                # Scale features
                scaled_features = self.scaler.transform(features_df)

                # Predict cheating using the ML model
                ml_prediction = self.model.predict(scaled_features)[0]

                overall_score = (
                        0.2 * text_sim_score +
                        0.4 * ast_sim_score +
                        0.2 * token_sim_score +
                        0.2 * lev_sim_score
                )

                if ml_prediction == 1 and overall_score > 0.7:
                    enhanced_results.append((file1, file2, overall_score, ml_prediction))

            self.detailed_results = enhanced_results

            return enhanced_results
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def get_cheating_report(self):
        results = self.analyze()
        if not results:
            print("No potential cheating detected.")
            return ["No potential cheating detected."]

        report = []
        for file1, file2, score, ml_prediction in results:
            report.append(
                f'Possible cheating between {file1} and {file2} '
                f'with an overall score of {score:.2f} and ML prediction: {ml_prediction}')
        return report

    def get_detailed_results(self):
        """
        Return the detailed results after analysis.
        """
        if not self.detailed_results:
            print("No detailed results available. Run analyze() first.")
        return self.detailed_results
