import unittest

INPUT_FILE_NAME = 'input.txt'
TEST_INPUT_FILE_NAME = 'input_test.txt'


def load_file_numbers(file_name):
    with open(file_name) as file:
        return [int(line.strip()) for line in file.readlines()]


def any_number_pair_sums_up_to(numbers, target):
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target and numbers[i] != numbers[j]:
                return True
    return False


def get_first_invalid_number(preamble_length, numbers):
    for i in range(preamble_length, len(numbers)):
        preamble = numbers[i - preamble_length:i]
        if not any_number_pair_sums_up_to(preamble, numbers[i]):
            return numbers[i]
    return None


class PartOneTest(unittest.TestCase):
    def test_get_first_invalid_number(self):
        numbers = load_file_numbers(TEST_INPUT_FILE_NAME)
        number = get_first_invalid_number(5, numbers)
        self.assertEqual(127, number)


def part_one():
    numbers = load_file_numbers(INPUT_FILE_NAME)
    number = get_first_invalid_number(25, numbers)
    print(f'The first invalid number is {number}')


def main():
    part_one()


if __name__ == '__main__':
    main()
    unittest.main()
