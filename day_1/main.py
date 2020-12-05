INPUT_FILE_NAME = 'input.txt'
ENTRIES_TARGET_SUM = 2020


def load_entries():
    with open(INPUT_FILE_NAME) as input_file:
        return [int(line.strip()) for line in input_file.readlines() if line.strip()]


def main():
    entries = load_entries()
    for i in range(0, len(entries)):
        for j in range(i + 1, len(entries)):
            first_entry = entries[i]
            second_entry = entries[j]
            entries_sum = first_entry + second_entry
            if entries_sum == ENTRIES_TARGET_SUM:
                print(f'Found entries ({first_entry},{second_entry}) that sum up to {ENTRIES_TARGET_SUM}')
                print(f'{first_entry} * {second_entry} = {first_entry * second_entry}')


if __name__ == '__main__':
    main()
