from functools import reduce

INPUT_FILE_NAME = 'input.txt'
TREE = '#'
OPEN = '.'


def all_arrays_same_len(rows):
    first_row_length = len(rows[0])
    return len([row for row in rows if len(row) == first_row_length]) == len(rows)


class EnvMap:
    def __init__(self, map_str):
        self.rows = [row.strip() for row in map_str.split('\n') if row.strip()]
        if not all_arrays_same_len(self.rows):
            raise Exception('Map string is malformed: all rows are expected to have the same length')
        self.height = len(self.rows)
        self.width = len(self.rows[0])

    def char_at(self, row, column):
        if row >= len(self.rows):
            return None
        elif column >= self.width:
            return self.rows[row][column % self.width]
        else:
            return self.rows[row][column]

    def __str__(self):
        return '\n'.join(self.rows)


def load_map():
    with open(INPUT_FILE_NAME) as input_file:
        return EnvMap(input_file.read())


def count_trees(env_map, slope):
    tree_count = 0
    location = (0, 0)
    while env_map.char_at(*location) is not None:
        char_at_location = env_map.char_at(location[0], location[1])
        if char_at_location == TREE:
            tree_count = tree_count + 1
        location = (location[0] + slope[0], location[1] + slope[1])
    return tree_count


def main_part_one():
    env_map = load_map()
    tree_count = count_trees(env_map, (1, 3))
    print(f'There are {tree_count} trees')


def main_part_two():
    slopes = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1)
    ]
    env_map = load_map()
    tree_counts = [count_trees(env_map, slope) for slope in slopes]
    print(f'Tree counts multiplied together is equal to {reduce(lambda x, y: x * y, tree_counts)}')


if __name__ == '__main__':
    main_part_one()
    main_part_two()