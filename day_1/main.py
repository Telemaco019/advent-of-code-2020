INPUT_FILE_NAME = 'input.txt'
ENTRIES_TARGET_SUM = 2020


def load_entries():
    with open(INPUT_FILE_NAME) as input_file:
        return [int(line.strip()) for line in input_file.readlines() if line.strip()]


def get_two_entries_matching_sum(entries, target_sum):
    for i in range(0, len(entries)):
        for j in range(i + 1, len(entries)):
            first_entry = entries[i]
            second_entry = entries[j]
            entries_sum = first_entry + second_entry
            if entries_sum == target_sum:
                return first_entry, second_entry
    return None


def get_three_entries_matching_sum(entries, target_sum):
    for i in range(0, len(entries)):
        for j in range(i + 1, len(entries)):
            for k in range(j + 1, len(entries)):
                first_entry = entries[i]
                second_entry = entries[j]
                third_entry = entries[k]
                entries_sum = first_entry + second_entry + third_entry
                if entries_sum == target_sum:
                    return first_entry, second_entry, third_entry
    return None


def main_part_one():
    entries = load_entries()
    result = get_two_entries_matching_sum(entries, ENTRIES_TARGET_SUM)
    if result is not None:
        first_entry, second_entry = result
        print(f'Found entries ({first_entry},{second_entry}) that sum up to {ENTRIES_TARGET_SUM}')
        print(f'{first_entry} * {second_entry} = {first_entry * second_entry}')
    else:
        print(f'Could not find entries summing up to {ENTRIES_TARGET_SUM}')


def main_part_two():
    entries = load_entries()
    result = get_three_entries_matching_sum(entries, ENTRIES_TARGET_SUM)
    if result is not None:
        first_entry, second_entry, third_entry = result
        print(f'Found entries ({first_entry},{second_entry},{third_entry}) that sum up to {ENTRIES_TARGET_SUM}')
        print(f'{first_entry} * {second_entry} * {third_entry} = {first_entry * second_entry * third_entry}')
    else:
        print(f'Could not find entries summing up to {ENTRIES_TARGET_SUM}')


if __name__ == '__main__':
    main_part_one()
    main_part_two()
