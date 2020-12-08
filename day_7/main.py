import re
import unittest

INPUT_FILE_NAME = 'input.txt'
TEST_INPUT_FILE_NAME = 'test_input.txt'


def load_file_lines(file_name):
    with open(file_name) as file:
        return file.readlines()


def flatten(input_list):
    result = []
    for i in input_list:
        if isinstance(i, list):
            result = result + flatten(i)
        else:
            result.append(i)
    return result


def replace_occurrence_num_with_bag_name(bag_name_with_occurrence):
    if bag_name_with_occurrence == 'no other':
        return []
    occurrences, bag_name = re.split('\s', bag_name_with_occurrence, 1)
    return [bag_name.strip() for _ in range(0, int(occurrences.strip()))]


def load_colors_and_children_dict(file_name):
    result = {}
    lines = [line.strip().replace('.', '') for line in load_file_lines(file_name) if line.strip()]
    for line in lines:
        (bag, contained_bags) = line.split('contain')
        contained_bags = [bag.strip() for bag in contained_bags.replace('bags', '').replace('bag', '').split(',')]
        contained_bags = [replace_occurrence_num_with_bag_name(contained_bag) for contained_bag in contained_bags]
        contained_bags = flatten(contained_bags)
        result.update({bag.replace('bags', '').strip(): contained_bags})
    return result


class Bag:
    def __init__(self, color):
        self.contained_bags = {}
        self.color = color

    def add_contained_bag(self, bag, count=1):
        self.contained_bags.update({bag: count})

    def __str__(self):
        return f'Color: {self.color}'

    def is_descendant_of(self, bag, hierarchy_map=None):
        if hierarchy_map is None:
            hierarchy_map = {}
        if hierarchy_map.get((self, bag)):
            return True
        elif len(bag.contained_bags) == 0:
            hierarchy_map[(self, bag)] = False
            return False
        elif self.color in [b.color for b in bag.contained_bags.keys()]:
            hierarchy_map[(self, bag)] = True
            return True
        else:
            return any(self.is_descendant_of(node, hierarchy_map) for node in bag.contained_bags.keys())

    def get_contained_bags_count(self):
        count = 0
        for contained_bag, contained_bag_occurrences in self.contained_bags.items():
            contained_bag_descendants_count = contained_bag.get_contained_bags_count()
            if contained_bag_descendants_count == 0:
                count += contained_bag_occurrences
            else:
                count += contained_bag_occurrences + contained_bag_occurrences * contained_bag_descendants_count
        return count


def load_all_bags(input_file_name):
    colors_with_children_dict = load_colors_and_children_dict(input_file_name)
    bags = [Bag(color) for color, _ in colors_with_children_dict.items()]
    for bag in bags:
        children_colors = colors_with_children_dict[bag.color]
        for child_color in set(children_colors):
            child_bag = next((b for b in bags if b.color == child_color), None)
            if child_bag is not None:
                child_bag_count = len([c for c in children_colors if c == child_bag.color])
                bag.add_contained_bag(child_bag, child_bag_count)
    return bags


class PartOneTest(unittest.TestCase):
    def test_counts(self):
        bags = load_all_bags(TEST_INPUT_FILE_NAME)
        shiny_gold_bag = next(b for b in bags if b.color == 'shiny gold')
        shiny_gold_containers_count = len(set([b for b in bags if shiny_gold_bag.is_descendant_of(b)]))
        self.assertEqual(shiny_gold_containers_count, 4)


class PartTwoTest(unittest.TestCase):
    def test_counts(self):
        bags = load_all_bags(TEST_INPUT_FILE_NAME)
        shiny_gold_bag = next(b for b in bags if b.color == 'shiny gold')
        self.assertEqual(shiny_gold_bag.get_contained_bags_count(), 32)


def part_one():
    bags = load_all_bags(INPUT_FILE_NAME)
    shiny_gold_bag = next(b for b in bags if b.color == 'shiny gold')
    shiny_gold_containers_count = len(set([b for b in bags if shiny_gold_bag.is_descendant_of(b)]))
    print(f'{shiny_gold_containers_count} different colors can contain {shiny_gold_bag.color} bag')


def part_two():
    bags = load_all_bags(INPUT_FILE_NAME)
    shiny_gold_bag = next(b for b in bags if b.color == 'shiny gold')
    print(f'{shiny_gold_bag.color} contains {shiny_gold_bag.get_contained_bags_count()} different bags')


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
    unittest.main()
