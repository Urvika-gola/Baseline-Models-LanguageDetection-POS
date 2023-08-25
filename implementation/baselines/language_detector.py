import argparse
import random
import re


def read_data(file):
    for sentence in file.readlines():
        sentence = sentence.rstrip()
        language, sentence = re.search("([a-z]{2}) (.*)", sentence).groups()
        yield language, sentence


def detect_language(sentence):
    """
    Detect the language of a document

    Args
        sentence: a tokenized sentence. Tokens are separated by white space.

    Returns:
        String indicating the language of sentence
          "en" if the document is en English
          "es" if the document is en Spanish
    """

    language = None
    # YOUR CODE GOES HERE. DO NOT MODIFY ANY OTHER METHOD IN ANY FILE
    # TODO Change the code below so the return value is not random
    #   You will get full credit as long as your implementation gets more than 85% accuracy
    #   Your implementation should be simple: a few if statements is all you need
    #   We will test your code with new sentences, so write a generic language detector
    en_frequent_word_set = {"the", "and", "is", "in", "of", "an"}
    es_frequent_word_set = {"el", "es", "en", "un", "de", "la", "se"}

    en_word_count = sum(1 for word in sentence.split() if word.lower() in en_frequent_word_set)
    es_word_count = sum(1 for word in sentence.split() if word.lower() in es_frequent_word_set)

    es_letters = any(char in "ñáéíóú¡¿" for char in sentence.lower())

    if en_word_count >= es_word_count:  # if the frequent english words are more than frequent spanish words
        language = "en"
    elif es_letters:  # if it contains spanish letters then surely its spanish
        language = "es"
    elif en_word_count < es_word_count:  # if the frequent spanish words are more than frequent english words
        language = "es"
    else:  # if none of the conditions match then default language is english as its more commonly used than spanish
        language = "en"
    assert language in ["en", "es"]
    return language

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Detect the language of document.')
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()

    predictions_correct = []
    for gold_language, sentence in read_data(args.file):
        pred_language = detect_language(sentence)

        if gold_language == pred_language:
            predictions_correct.append(1)
        else:
            predictions_correct.append(0)

        print(f"PRED: {pred_language} | GOLD : {gold_language} | {sentence}")

    print("*" * 40)
    print(f"  Accuracy: {sum(predictions_correct) / len(predictions_correct):.2f}"
          f"[{sum(predictions_correct)}/{len(predictions_correct)}]")
