import string
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
        self.answers_by_person = [answer.strip() for answer in answers_str.split('\n') if answer.strip()]
        self.all_answers = flatten([list(answers) for answers in self.answers_by_person])

    def get_distinct_answers_count(self):
        return len(set(self.all_answers))

    def get_answers_intersection_count(self):
        answers_intersection = []
        for answer in string.ascii_lowercase:
            if all(answer in person_answers_list for person_answers_list in self.answers_by_person):
                answers_intersection.append(answer)
        return len(answers_intersection)


def load_groups(input_file_name):
    input_str = load_file_as_str(input_file_name)
    return [Group(group_str) for group_str in input_str.split('\n\n') if group_str.strip()]


class PartOneTest(unittest.TestCase):
    def test_counts(self):
        groups = load_groups(TEST_INPUT_FILE)
        answers_sum = sum([group.get_distinct_answers_count() for group in groups])
        self.assertEqual(answers_sum, 11)


class PartTwoTest(unittest.TestCase):
    def test_counts(self):
        groups = load_groups(TEST_INPUT_FILE)
        answers_sum = sum([group.get_answers_intersection_count() for group in groups])
        self.assertEqual(answers_sum, 6)


def main():
    groups = load_groups(INPUT_FILE)
    answers_sum_part_one = sum([group.get_distinct_answers_count() for group in groups])
    answers_sum_part_two = sum([group.get_answers_intersection_count() for group in groups])

    print(f'The sum of the counts for part 1 is {answers_sum_part_one}')
    print(f'The sum of the counts for part 2 is {answers_sum_part_two}')


if __name__ == '__main__':
    main()
    unittest.main()
