import tokenize
from io import StringIO


class Tokenizer:
    def tokenize_code(self, code):
        tokens = []
        reader = StringIO(code).readline
        for token in tokenize.generate_tokens(reader):
            if token.type in (tokenize.NAME, tokenize.NUMBER):
                tokens.append((token.type, "_token"))
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
