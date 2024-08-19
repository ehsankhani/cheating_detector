from difflib import SequenceMatcher


class SimilarityDetector:
    def __init__(self, files):
        self.files = files

    def calculate_similarity(self, code1, code2):
        return SequenceMatcher(None, code1, code2).ratio()

    def detect_similarities(self):
        similarities = []
        filenames = list(self.files.keys())
        for i in range(len(filenames)):
            for j in range(i + 1, len(filenames)):
                sim_score = self.calculate_similarity(self.files[filenames[i]], self.files[filenames[j]])
                if sim_score > 0.5:  # Threshold for probable cheating
                    similarities.append((filenames[i], filenames[j], sim_score))
        return similarities
