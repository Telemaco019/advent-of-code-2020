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
        self.contained_bags = []
        self.color = color

    def add_contained_bag(self, bag):
        self.contained_bags.append(bag)

    def __str__(self):
        return f'Color: {self.color}'


def load_all_bags(input_file_name):
    colors_with_children_dict = load_colors_and_children_dict(input_file_name)
    bags = [Bag(color) for color, _ in colors_with_children_dict.items()]
    for bag in bags:
        children_colors = colors_with_children_dict[bag.color]
        for child_color in children_colors:
            child_bag = next((b for b in bags if b.color == child_color), None)
            if child_bag is not None and child_bag not in bag.contained_bags:
                bag.add_contained_bag(child_bag)
    return bags


def is_descendant(child: Bag, parent: Bag, hierarchy_map={}):
    if hierarchy_map.get((child, parent)):
        return True
    elif len(parent.contained_bags) == 0:
        hierarchy_map[(child, parent)] = False
        return False
    elif child.color in [b.color for b in parent.contained_bags]:
        hierarchy_map[(child, parent)] = True
        return True
    else:
        return any(is_descendant(child, node, hierarchy_map) for node in parent.contained_bags)


class PartOneTest(unittest.TestCase):
    def test_counts(self):
        bags = load_all_bags(TEST_INPUT_FILE_NAME)
        shiny_gold_bag = next(b for b in bags if b.color == 'shiny gold')
        shiny_gold_containers_count = len(set([b for b in bags if is_descendant(shiny_gold_bag, b)]))
        self.assertEqual(shiny_gold_containers_count, 4)


def main():
    bags = load_all_bags(INPUT_FILE_NAME)
    shiny_gold_bag = next(b for b in bags if b.color == 'shiny gold')
    shiny_gold_containers_count = len(set([b for b in bags if is_descendant(shiny_gold_bag, b)]))
    print(f'{shiny_gold_containers_count} different colors can contain {shiny_gold_bag.color} bag')


if __name__ == '__main__':
    main()
    unittest.main()
