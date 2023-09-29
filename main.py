from text_processing import read_text, tokenize

if __name__ == '__main__':
    text = read_text('text.txt')
    sentences = tokenize(text)
    print(sentences)

