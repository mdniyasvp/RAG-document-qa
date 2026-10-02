import re 

class KeywordSearch:
    @staticmethod
    def tokenize(text:str) -> list[str]:
        return re.findall(r"\b\w+\b", text.lower())

    def score(self, query: str, document:str) -> float:
        query_tokens = set(self.tokenize(query))
        document_tokens = set(self.tokenize(document))

        if not query_tokens:
            return 0.0

        matched_tokens = query_tokens.intersection(document_tokens)

        return len(matched_tokens) / len(query_tokens)