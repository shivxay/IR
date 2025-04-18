document1 = "The quick brown fox jumped over the lazy dog"
document2 = "The lazy dog slept in the sun"

import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

# Tokenize and filter stopwords
tokens1 = [word for word in document1.lower().split() if word not in stop_words]
tokens2 = [word for word in document2.lower().split() if word not in stop_words]

# Build inverted index and occurrence counts
inverted_index = {}
occurrences = {"Document 1": {}, "Document 2": {}}

for term in set(tokens1 + tokens2):
    inverted_index[term] = []
    if term in tokens1:
        inverted_index[term].append("Document 1")
        occurrences["Document 1"][term] = tokens1.count(term)
    if term in tokens2:
        inverted_index[term].append("Document 2")
        occurrences["Document 2"][term] = tokens2.count(term)

# Print results
print("Inverted Index:", inverted_index)
print("Occurrences in Document 1:", occurrences["Document 1"])
print("Occurrences in Document 2:", occurrences["Document 2"])

# Print inverted index with occurrences
for term, docs in inverted_index.items():
    print(f"{term} ->", end="")
    print(", ".join(f"{doc}({occurrences[doc].get(term, 0)})" for doc in docs))

print("Performed by Shivam Vishwakarma")

