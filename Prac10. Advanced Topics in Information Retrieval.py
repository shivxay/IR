#Implement a text summarization algorithm (e.g., extractive or abstractive). 
#Build a question-answering system using techniques such as information extractionimport nltk

import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter

def generate_summary(text, num_sentences=2):
    sentences = sent_tokenize(text)
    words = [word.lower() for word in word_tokenize(text) if word.isalnum()]
    words = [word for word in words if word not in stopwords.words("english")]
    
    word_freq = Counter(words)
    sentence_scores = {sent: sum(word_freq[word] for word in word_tokenize(sent.lower()) if word in word_freq) for sent in sentences}
    
    summary = ' '.join(sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences])
    return summary

# Example usage
text = """
Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics concerned with the interactions between computers and human (natural) languages. 
As such, NLP is related to the area of human–computer interaction. 
Many challenges in NLP involve natural language understanding, that is, enabling computers to derive meaning from human or natural language input, and others involve natural language generation.
"""
print(generate_summary(text))
