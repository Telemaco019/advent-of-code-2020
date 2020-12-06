import unittest

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'input_test.txt'


def load_file_as_str(filename):
    with open(filename) as file:
        return file.read()


def flatten(input_list):
    result = []
    for i in input_list:
        if isinstance(i, list):
            result = result + flatten(i)
        else:
            result.append(i)
    return result


class Group:
    def __init__(self, answers_str):
        answers_by_person = [answer.strip() for answer in answers_str.split('\n') if answer.strip()]
        self.answers = flatten([list(answers) for answers in answers_by_person])

    def get_distinct_answers_count(self):
        return len(set(self.answers))


def load_groups(input_file_name):
    input_str = load_file_as_str(input_file_name)
    return [Group(group_str) for group_str in input_str.split('\n\n') if group_str.strip()]


class PartOneTest(unittest.TestCase):
    def test_counts(self):
        groups = load_groups(TEST_INPUT_FILE)
        answers_sum = sum([group.get_distinct_answers_count() for group in groups])
        self.assertEqual(answers_sum, 11)


def main():
    groups = load_groups(INPUT_FILE)
    answers_sum = sum([group.get_distinct_answers_count() for group in groups])
    print(f'The sum of the counts is {answers_sum}')


if __name__ == '__main__':
    main()
    unittest.main()
