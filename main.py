import numpy as np

from text_processing import read_text, tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

if __name__ == '__main__':
    text = read_text('text.txt')
    sentences = tokenize(text)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform([' '.join(sentence) for sentence in sentences])
    print(list(X[0]))

