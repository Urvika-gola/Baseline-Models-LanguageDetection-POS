from baselines.pos_tagger import run_tagger


def run_test(file_path, gold_path, min_accuracy):
    accuracy = run_tagger(file_path, gold_path, quiet=True)
    assert accuracy >= min_accuracy, \
        f"The accuracy is {accuracy}, which is less than {min_accuracy}"


# def run_test_pos_small(min_accuracy):
#     file_path = "implementation/baselines/data/pos_tagger/en_tokenized.txt"
#     gold_path = "implementation/baselines/data/pos_tagger/en_tokenized_withPOS.txt"
#     run_test(open(file_path, 'r'), open(gold_path, 'r'), min_accuracy)
#
#
# def test_pos_small_10():
#     run_test_pos_small(0.1)
#
#
# def test_pos_small_20():
#     run_test_pos_small(0.2)
#
#
# def test_pos_small_30():
#     run_test_pos_small(0.3)
#
#
# def test_pos_small_40():
#     run_test_pos_small(0.4)
#
#
# def test_pos_small_50():
#     run_test_pos_small(0.5)


def run_test_pos_large(min_accuracy):
    file_path = "implementation/baselines/data/pos_tagger/en_tokenized_large.txt"
    gold_path = "implementation/baselines/data/pos_tagger/en_tokenized_large_withPOS.txt"
    run_test(open(file_path, 'r'), open(gold_path, 'r'), min_accuracy)


def test_pos_large_10():
    run_test_pos_large(0.1)


def test_pos_large_20():
    run_test_pos_large(0.2)


def test_pos_large_30():
    run_test_pos_large(0.3)


def test_pos_large_35():
    run_test_pos_large(0.35)
