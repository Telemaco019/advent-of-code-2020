import math
import unittest

INPUT_FILE_NAME = 'input.txt'

FRONT_CHAR = 'F'
BACK_CHAR = 'B'
LEFT_CHAR = 'L'
RIGHT_CHAR = 'R'
PLANE_ROWS = 127
PLANE_COLUMNS = 7


def load_boarding_pass_list():
    with open(INPUT_FILE_NAME) as file:
        return [line.strip() for line in file.readlines() if line.strip()]


def split_list(a_list):
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]


def get_corresponding_index(char_seq, upper_half_char, lower_half_char, lowest_index, highest_index):
    lower_index, upper_index = lowest_index, highest_index

    for char in char_seq[:-1]:
        seq_range = upper_index - lower_index
        if char == lower_half_char:
            (lower_index, upper_index) = (lower_index, lower_index + seq_range // 2)
        if char == upper_half_char:
            (lower_index, upper_index) = (lower_index + math.ceil(seq_range / 2), upper_index)

    if char_seq[-1] == lower_half_char:
        return lower_index
    elif char_seq[-1] == upper_half_char:
        return upper_index
    else:
        return -1


def get_boarding_pass_id(boarding_pass):
    row_chars = boarding_pass[:-3]
    column_chars = boarding_pass[-3:]
    row_index = get_corresponding_index(row_chars, BACK_CHAR, FRONT_CHAR, 0, PLANE_ROWS)
    column_index = get_corresponding_index(column_chars, RIGHT_CHAR, LEFT_CHAR, 0, PLANE_COLUMNS)
    return row_index * 8 + column_index


class TestBoardingPassIdGeneration(unittest.TestCase):
    def test_id(self):
        first_generated = get_boarding_pass_id('FBFBBFFRLR')
        self.assertEqual(first_generated, 357)

        second_generated = get_boarding_pass_id('BFFFBBFRRR')
        self.assertEqual(second_generated, 567)

        third_generated = get_boarding_pass_id('FFFBBBFRRR')
        self.assertEqual(third_generated, 119)

        fourth_generated = get_boarding_pass_id('BBFFBBFRLL')
        self.assertEqual(fourth_generated, 820)


def main():
    boarding_pass_list = load_boarding_pass_list()
    boarding_pass_id_list = [get_boarding_pass_id(boarding_pass) for boarding_pass in boarding_pass_list]
    print(f'The highest id is {max(boarding_pass_id_list)}')


if __name__ == '__main__':
    main()
    unittest.main()
