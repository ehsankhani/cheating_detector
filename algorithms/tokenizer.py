import tokenize
from io import StringIO
import keyword


class EnhancedTokenizer:
    def __init__(self):
        self.keywords = set(keyword.kwlist)

    def tokenize_code(self, code):
        tokens = []
        reader = StringIO(code).readline
        for token in tokenize.generate_tokens(reader):
            if token.type == tokenize.NAME:
                if token.string in self.keywords:
                    tokens.append((token.type, token.string))
                else:
                    tokens.append((token.type, "_name"))  # Normalize variable and function names
            elif token.type == tokenize.NUMBER:
                tokens.append((token.type, "_number"))  # Normalize all numbers
            elif token.type == tokenize.STRING:
                tokens.append((token.type, "_string"))  # Normalize all strings
            elif token.type == tokenize.COMMENT:
                tokens.append((token.type, "_comment"))  # Normalize comments
            else:
                tokens.append((token.type, token.string))
        return tokens

    def compare_tokens(self, code1, code2):
        tokens1 = self.tokenize_code(code1)
        tokens2 = self.tokenize_code(code2)
        return self._token_similarity(tokens1, tokens2)

    def _token_similarity(self, tokens1, tokens2):
        match_count = sum(1 for t1, t2 in zip(tokens1, tokens2) if t1 == t2)
        return match_count / max(len(tokens1), len(tokens2))
