import re
from collections import defaultdict

class DocumentRetrievalSystem:
    def __init__(self):
        self.index = defaultdict(list)
        self.documents = []

    def add_documents(self, documents):
        for doc_id, document in enumerate(documents):
            self.documents.append(document)
            for term in self.tokenize(document):
                self.index[term].append(doc_id)

    def search(self, query):
        query_terms = self.tokenize(query)
        result_docs = set(self.index[query_terms[0]]) if query_terms and query_terms[0] in self.index else set()
        for term in query_terms[1:]:
            result_docs &= set(self.index[term])
        return [self.documents[doc_id] for doc_id in result_docs]

    @staticmethod
    def tokenize(text):
        return re.findall(r'\b\w+\b', text.lower())

if __name__ == "__main__":
    retrieval_system = DocumentRetrievalSystem()
    retrieval_system.add_documents([
        "This is the first document",
        "Python is a popular programming language",
        "Document retrieval systems are important"
    ])

    query = "is"
    results = retrieval_system.search(query)

    if results:
        print(f"Search results for '{query}':")
        for result in results:
            print("-", result)
    else:
        print(f"No results found for '{query}'.")
