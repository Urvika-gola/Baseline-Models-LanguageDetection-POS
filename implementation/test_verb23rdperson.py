from verbs_23rdperson.verb23rdperson import read_verbs
from verbs_23rdperson.verb23rdperson import get_3rdperson


def read_gold(file_path):
    with open(file_path) as f:
        for line in f.readlines():
            line = line.rstrip()
            if len(line) < 1:
                continue
            verb, verb3rdperson = line.split()
            print(verb3rdperson)
            yield verb3rdperson.rstrip()


def run_test(verbs_path, gold_path):
    verbs = list(read_verbs(verbs_path))
    gold = list(read_gold(gold_path))
    if not len(verbs):
        assert False, f"{verbs_path}  is empty. It is your job to add new test cases to test your code"
    if not len(gold):
        assert False, f"{gold_path}  is empty. It is your job to add new test cases to test your code"
    for verb, gold in zip(verbs, gold):
        assert get_3rdperson(verb) == gold


def test_public():
    verbs_path = "implementation/verbs_23rdperson/verbs.txt"
    gold_path = "implementation/verbs_23rdperson/verbs.txt.output"
    run_test(verbs_path, gold_path)


def test_addtl():
    verbs_path = "implementation/verbs_23rdperson/verbs.addtl.txt"
    gold_path = "implementation/verbs_23rdperson/verbs.addtl.txt.output"
    run_test(verbs_path, gold_path)
