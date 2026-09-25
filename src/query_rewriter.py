class QueryRewriter:

    def rewrite(self, query: str) -> str:
        query = query.strip()

        if not query:
            raise ValueError("Query cannot be empty.")

        replacements = {
            "how many days?": "How many annual leave days are employees entitled to?",
            "how many days": "How many annual leave days are employees entitled to?",
            "what about leave?": "What is the company's annual leave policy?",
        }

        normalized_query = query.lower()

        return replacements.get(
            normalized_query,
            query,
        )