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


def get_invalid_numbers(preamble_length, numbers):
    result = []
    for i in range(preamble_length, len(numbers)):
        preamble = numbers[i - preamble_length:i]
        if not any_number_pair_sums_up_to(preamble, numbers[i]):
            result.append((i, numbers[i]))
    return result


def get_first_invalid_number(preamble_length, numbers):
    invalid_numbers = get_invalid_numbers(preamble_length, numbers)
    if len(invalid_numbers) == 0:
        return None
    else:
        return invalid_numbers[0]


def get_encryption_weakness(preamble_length, numbers):
    (index, number) = get_first_invalid_number(preamble_length, numbers)
    continuous_range = []
    range_start, range_end = (min(0, index - preamble_length), index - 1)
    for i in range(range_start, range_end):
        for j in range(i, range_end):
            if sum(numbers[i:j]) == number:
                continuous_range += numbers[i:j]
    return min(continuous_range) + max(continuous_range)


class PartOneTest(unittest.TestCase):
    def test_get_first_invalid_number(self):
        numbers = load_file_numbers(TEST_INPUT_FILE_NAME)
        number = get_first_invalid_number(5, numbers)[1]
        self.assertEqual(127, number)


class PartTwoTest(unittest.TestCase):
    def test_get_encryption_weakness(self):
        numbers = load_file_numbers(TEST_INPUT_FILE_NAME)
        weakness = get_encryption_weakness(5, numbers)
        self.assertEqual(62, weakness)


def part_one():
    numbers = load_file_numbers(INPUT_FILE_NAME)
    number = get_first_invalid_number(25, numbers)
    print(f'The first invalid number is {number}')


def part_two():
    numbers = load_file_numbers(INPUT_FILE_NAME)
    weakness = get_encryption_weakness(25, numbers)
    print(f'The weakness is {weakness}')


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
    unittest.main()
