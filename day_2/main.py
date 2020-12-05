from abc import ABCMeta, abstractmethod

INPUT_FILE_NAME = 'input.txt'


class PasswordPolicy(metaclass=ABCMeta):
    @abstractmethod
    def is_satisfied_by(self, pwd_str: str):
        pass


class PartOnePasswordPolicy(PasswordPolicy):
    def __init__(self, policy: str):
        min_and_max_occurrences, letter = policy.split(' ')
        self.policy_letter = letter
        self.letter_min_occurrences, self.letter_max_occurrences = [int(i) for i in min_and_max_occurrences.split('-')]

    def __str__(self):
        return f'{self.letter_min_occurrences}-{self.letter_max_occurrences} {self.policy_letter}'

    def is_satisfied_by(self, pwd_str):
        letter_occurrences = pwd_str.count(self.policy_letter)
        return self.letter_min_occurrences <= letter_occurrences <= self.letter_max_occurrences


class PartTwoPasswordPolicy(PasswordPolicy):
    def __init__(self, policy: str):
        first_and_second_index, letter = policy.split(' ')
        self.policy_letter = letter
        self.first_index, self.second_index = [int(i) - 1 for i in first_and_second_index.split('-')]

    def __str__(self):
        return f'{self.first_index}-{self.second_index} {self.policy_letter}'

    def is_satisfied_by(self, pwd_str: str):
        first_index_letter = pwd_str[self.first_index]
        second_index_letter = pwd_str[self.second_index]
        if first_index_letter == self.policy_letter and second_index_letter == self.policy_letter:
            return False
        elif first_index_letter == self.policy_letter or second_index_letter == self.policy_letter:
            return True
        else:
            return False


class Password:
    def __init__(self, pwd: str, policy: PartOnePasswordPolicy):
        self.__pwd_str = pwd
        self.__policy = policy

    def is_valid(self):
        return self.__policy.is_satisfied_by(self.__pwd_str)

    def __repr__(self):
        return f'Password: {self.__pwd_str} - Policy: {self.__policy}'


def load_input_lines():
    with open(INPUT_FILE_NAME) as input_file:
        return [line.strip() for line in input_file.readlines() if line.strip()]


def load_passwords_list(create_policy_from_str):
    passwords_list = []
    for line in load_input_lines():
        policy_str, pwd_str = line.split(':')
        policy = create_policy_from_str(policy_str.strip())
        password = Password(pwd_str.strip(), policy)
        passwords_list.append(password)
    return passwords_list


def main():
    passwords_list = load_passwords_list(lambda policy_string: PartTwoPasswordPolicy(policy_string))
    valid_passwords = [pwd for pwd in passwords_list if pwd.is_valid()]
    print(f'There are {len(valid_passwords)} valid passwords')


if __name__ == '__main__':
    main()
