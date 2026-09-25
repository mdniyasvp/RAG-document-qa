from src.query_rewriter import QueryRewriter


rewriter = QueryRewriter()


queries = [
    "How many days?",
    "What about leave?",
    "What is the annual leave policy?",
]


for query in queries:

    rewritten_query = rewriter.rewrite(query)

    print("\nOriginal:")
    print(query)

    print("Rewritten:")
    print(rewritten_query)