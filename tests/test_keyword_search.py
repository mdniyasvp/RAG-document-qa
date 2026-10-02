from src.keyword_search import KeywordSearch


search = KeywordSearch()


query = "annual leave policy"

documents = [
    "Employees are entitled to annual leave according to company policy.",
    "Employees receive medical benefits.",
    "The company has an annual performance review.",
]


for document in documents:

    score = search.score(
        query,
        document,
    )

    print("\nDocument:")
    print(document)

    print("Keyword score:")
    print(score)