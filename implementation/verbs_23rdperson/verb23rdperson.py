import argparse
import re


def read_verbs(file_path):
    with open(file_path) as f:
        for verb in f.readlines():
            verb = verb.rstrip()
            if len(verb) < 1:
                continue
            yield verb.rstrip()


def get_3rdperson(verb):
    # YOUR CODE GOES HERE. DO NOT MODIFY ANY OTHER METHOD IN ANY FILE
    # Use the re package to do string matching. A good solution is as short as 5 lines
    # You are responsible for adding additional test cases in verbs.addtl.txt and verbs.addtl.txt.output.
    #    We will test your implementation with new examples (and deduct points if you don't get them right)
    #    We won't give partial credit for this question.

    # Remove any white spaces and convert to lowercase
    verb = verb.strip().lower()
    if re.search(r'(ss|x|ch|sh|o)$', verb):
        return verb + 'es'
    elif re.search(r'[^aeiou]y$',verb):
        return re.sub('y$', 'ies', verb)
    else:
        return verb + 's'


def process_file(file_path):
    for verb in read_verbs(file_path):

        yield verb, get_3rdperson(verb)


def main(file_path):
    for verb, verb3rdperson in process_file(file_path):
        print(f"{verb:10} {verb3rdperson}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("FILE_PATH",
                        help="Path to file with verbs in their base form, one verb per line")
    args = parser.parse_args()

    main(args.FILE_PATH)