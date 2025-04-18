documents = {
    1: "apple banana orange",
    2: "apple banana",
    3: "banana orange",
    4: "apple",
}

def build_index(docs):
    index = {}
    for doc_id, text in docs.items():
        for term in set(text.split()):
            index.setdefault(term, set()).add(doc_id)
    return index

inverted_index = build_index(documents)

def boolean_and(operands, index):
    result = index.get(operands[0], set())
    for term in operands[1:]:
        result &= index.get(term, set())
    return list(result)

def boolean_or(operands, index, total_docs):
    result = set()
    for term in operands:
        result |= index.get(term, set())
    return list(result | set(range(1, total_docs + 1)))

def boolean_not(operand, index, total_docs):
    return list(set(range(1, total_docs + 1)) - index.get(operand, set()))

query1, query2, query3 = ["apple", "banana"], ["apple", "orange"], "orange"
print("AND:", boolean_and(query1, inverted_index))
print("OR:", boolean_or(query2, inverted_index, len(documents)))
print("NOT:", boolean_not(query3, inverted_index, len(documents)))
