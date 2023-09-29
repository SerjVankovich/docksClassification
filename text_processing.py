import string
import re

import nltk
nltk.download('wordnet')


def read_text(path: str):
    with open(path, encoding='utf-8') as file:
        return file.read()


def tokenize(text: str):
    text = text.replace('\n\n', '. ')

    sentences = nltk.sent_tokenize(text, language='russian')
    sentences = [process_sentence(sentence) for sentence in sentences]
    print(sentences)


def replace_time_label(sentence: str):
    return re.sub(r'^\[\d\d:\d\d]', '', sentence).strip()


def process_sentence(sentence: str):
    sentence = replace_time_label(sentence)
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))

    words = nltk.word_tokenize(sentence, 'russian')
    lemmatizer = nltk.stem.WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in words]
