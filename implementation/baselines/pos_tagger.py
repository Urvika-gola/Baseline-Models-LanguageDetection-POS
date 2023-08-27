import argparse
import re


def tagger(file):
    """
    Detect the language of a document

    Args
        file: a file with one sentence per line. Tokens are separated by white space.

    Returns:
        Generator of sentences in file with part-of-speech tagged tokens. Each token is in the format "word/POS_TAG"
    """
    # YOUR CODE GOES HERE. DO NOT MODIFY ANY OTHER METHOD IN ANY FILE
    # TODO Change the code below so that not all tokens are assigned the NN part-of-speech tag (Noun, singular or mass)
    #   See the full tagset here: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    #   Hint: hard code with an if statement words that are common and easy to assign part-of-speech tags to.
    #   For example, "the" is always a DT (determiner) and words ending in "ly" tend to be RB (adverbs)
    #   Your are implementing a baseline, which has to be simple: a few if statement is all you need.
    #   We will test your code with additional sentences, so aim at a generic part-of-speech tagger for English
    #   An acceptable accuracy is above 35% with the large file (which has 1093 tokens)

    for sentence in file.readlines():
        sentence = sentence.rstrip()
        tokens = sentence.split(" ")
        pos_tags = []
        for token in tokens:
            if token.lower() in ["a", "an", "the", "this", "that", "these", "those"]:
                pos = "DT"
            elif token.lower() in ["is", "am", "are", "was", "were", "have", "has", "had", "do", "does", "did", "will", "would", "shall", "should", "can", "could"]:
                pos = "VB"
            elif token.lower() in ["and", "or", "but", "yet", "so", "nor", "for"]:
                pos = "CC"
            elif token.lower() in ["i", "you", "he", "she", "myself", "themselves", "somebody"]:
                pos = "PRON"
            elif token.lower() in ["he", "she", "it", "they", "we", "you", "i", "him", "her", "us", "them", "me"]:
                pos = "PRP"
            elif token.lower() in ["in", "on", "at", "by", "with", "about", "against", "into", "through", "during",
                                   "before", "after", "above", "below", "to", "from", "up", "down", "over", "under",
                                   "again", "further", "then", "once"]:
                pos = "IN"
            elif token.endswith("ing") or token.endswith("ed"):
                pos = "VERB"
            elif token.endswith("ous") or token.endswith("ful"):
                pos = "JJ"
            elif token.endswith("ly"):
                pos = "ADV"
            elif token.istitle():
                pos = "PROPN"
            elif token.isnumeric() or token.replace(".", "").isnumeric() or token.isdigit():
                pos = "CD"
            elif token.endswith("ly"):
                pos = "RB"
            elif token is ",":
                pos = ","
            elif token is ".":
                pos = "."
            # elif "-" in token:
            #     pos = "JJ"
            else:
                pos = "NN"
            pos_tags.append(pos)
        yield " ".join([f"{t}/{p}" for t, p in zip(tokens, pos_tags)])
def run_tagger(f, f_gold, quiet=False):
    num_tokens = 0
    num_tokens_correct = 0
    for tagged_sentence, gold_sentence in zip(tagger(f), f_gold.readlines()):
        gold_sentence = gold_sentence.rstrip()
        tagged_tokens = tagged_sentence.split(" ")
        gold_tokens = gold_sentence.split(" ")
        for tagged_token, gold_token in zip(tagged_tokens, gold_tokens):
            t_word, t_tag = tagged_token.split("/")
            g_word, g_tag = gold_token.split("/")
            assert t_word == g_word
            if t_tag == g_tag:
                num_tokens_correct += 1
            num_tokens += 1
        if not quiet:
            print(f"PRED: {tagged_sentence}")
            print(f"GOLD: {gold_sentence}")
            print("*" * 40)
    accuracy = num_tokens_correct / num_tokens
    if not quiet:
        print(f"  Accuracy: {accuracy:.2f} [{num_tokens_correct}/{num_tokens}]")
    return accuracy


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Detect the language of document.')
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('file_gold', type=argparse.FileType('r'))
    parser.add_argument('-q', '--quiet', action='store_true', help="Only output the accuracy")
    args = parser.parse_args()
    run_tagger(args.file, args.file_gold, args.quiet)
