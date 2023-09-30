import string

from nltk.corpus import stopwords
from pymystem3 import Mystem

import nltk

mystem = Mystem()
russian_stopwords = stopwords.words("russian")


def read_text(path: str):
    with open(path, encoding='utf-8') as file:
        lines = [line for line in file.readlines() if line != '\n']
        return lines


def tokenize(lines: list):
    result_sentences = []
    for line in lines:
        sentences = nltk.sent_tokenize(line, language='russian')
        result_sentences = result_sentences + sentences
    result_sentences = [process_sentence(sentence) for sentence in result_sentences]
    return result_sentences


def letters_not_punktuation(word):
    for letter in word:
        if letter in string.punctuation:
            return False
    return True


def process_sentence(sentence: str):
    words = mystem.lemmatize(sentence)

    return [word.strip() for word in words if word not in russian_stopwords
            and word not in [' ', '\n']
            and word.strip() not in string.punctuation
            and letters_not_punktuation(word)]
