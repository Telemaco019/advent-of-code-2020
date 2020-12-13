import unittest

INPUT_FILE_NAME = 'input.txt'
TEST_INPUT_FILE_NAME = 'test_input.txt'

ADAPTER_JOLTAGE_MAX_DIFFERENCE = 3
CHARGING_OUTLET_JOLTAGE = 0


def load_adapters_outputs(input_file_name):
    with open(input_file_name) as file:
        return sorted([int(line.strip()) for line in file.readlines() if line.strip()])


def compute_jolt_differences_distribution(input_file_name):
    differences_dict = {}
    sorted_outputs = load_adapters_outputs(input_file_name)
    joltage_list = [0] + sorted_outputs + [sorted_outputs[-1] + 3]
    for i in range(0, len(joltage_list) - 1):
        difference = joltage_list[i + 1] - joltage_list[i]
        differences_dict[difference] = differences_dict.get(difference, 0) + 1
    return differences_dict


class PartOneTest(unittest.TestCase):
    def test_jolt_differences_dist(self):
        differences_dict = compute_jolt_differences_distribution(TEST_INPUT_FILE_NAME)
        self.assertEqual(22 * 10, differences_dict[1] * differences_dict[3])


def part_one():
    differences_dict = compute_jolt_differences_distribution(INPUT_FILE_NAME)
    result = differences_dict[1] * differences_dict[3]
    print(f'The number of 1-jolt differences multiplied by the number of 3-jolt differences is {result}')


def main():
    part_one()


if __name__ == '__main__':
    main()
    unittest.main()
