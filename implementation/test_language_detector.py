from baselines.language_detector import detect_language
from baselines.language_detector import read_data


def run_lang_test(file_path, min_accuracy):
    with open(file_path) as f:
        preds, gold = [], []
        for language, sentence in read_data(f):
            gold.append(language)
            preds.append(detect_language(sentence))
        if not len(gold):
            assert False, f"{file_path} is empty. It is your job to add new test cases to test your code"
        correct = sum([1 if p == g else 0 for p, g in zip(preds, gold)])
        accuracy = correct / len(gold)
        assert accuracy >= min_accuracy,\
            f"The accuracy is {accuracy}, which is less than {min_accuracy}"


def run_lang_public_test(min_accuracy):
    file_path = "implementation/baselines/data/language_detector/sentences_en_es.txt"
    run_lang_test(file_path, min_accuracy)


def test_lang_public_40():
    run_lang_public_test(0.4)


def test_lang_public_50():
    run_lang_public_test(0.5)


def test_lang_public_60():
    run_lang_public_test(0.6)


def test_lang_public_70():
    run_lang_public_test(0.7)


def test_lang_public_80():
    run_lang_public_test(0.8)


def test_lang_public_90():
    run_lang_public_test(0.9)


def run_lang_addtl_test(min_accuracy):
    file_path = "implementation/baselines/data/language_detector/sentences_en_es.addtl.txt"
    run_lang_test(file_path, min_accuracy)


# def test_lang_addtl_40():
#     run_lang_addtl_test(0.4)
#
#
# def test_lang_addtl_50():
#     run_lang_addtl_test(0.5)
#
#
# def test_lang_addtl_60():
#     run_lang_addtl_test(0.6)
#
#
# def test_lang_addtl_70():
#     run_lang_addtl_test(0.7)
#
#
# def test_lang_addtl_80():
#     run_lang_addtl_test(0.8)


def test_lang_addtl_90():
    run_lang_addtl_test(0.90)
