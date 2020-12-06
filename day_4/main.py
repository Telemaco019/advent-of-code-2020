from abc import ABCMeta, abstractmethod

INPUT_FILE_NAME = 'input.txt'

FIELD_BIRTH_YEAR = 'byr'
FIELD_ISSUE_YEAR = 'iyr'
FIELD_EXPIRATION_YEAR = 'eyr'
FIELD_HEIGHT = 'hgt'
FIELD_HAIR_COLOR = 'hcl'
FIELD_EYE_COLOR = 'ecl'
FIELD_PASSPORT_ID = 'pid'
FIELD_COUNTRY_ID = 'cid'


def read_file_as_str(filename):
    with open(filename) as file:
        return file.read()


class Passport:
    def __init__(self, passport_str):
        fields_with_value = {field_value.split(':')[0]: field_value.split(':')[1]
                             for field_value in
                             passport_str.replace('\n', ' ').split(' ')}
        self.birth_year = fields_with_value.get(FIELD_BIRTH_YEAR)
        self.issue_year = fields_with_value.get(FIELD_ISSUE_YEAR)
        self.expiration_year = fields_with_value.get(FIELD_EXPIRATION_YEAR)
        self.height = fields_with_value.get(FIELD_HEIGHT)
        self.hair_color = fields_with_value.get(FIELD_HAIR_COLOR)
        self.eye_color = fields_with_value.get(FIELD_EYE_COLOR)
        self.passport_id = fields_with_value.get(FIELD_PASSPORT_ID)
        self.country_id = fields_with_value.get(FIELD_COUNTRY_ID)

    def is_valid(self):
        if self.birth_year is None: return False
        if self.issue_year is None: return False
        if self.expiration_year is None: return False
        if self.height is None: return False
        if self.hair_color is None: return False
        if self.eye_color is None: return False
        if self.passport_id is None: return False
        return True


def main():
    input_file_content = read_file_as_str(INPUT_FILE_NAME)
    passports = [Passport(passport_str) for passport_str in input_file_content.split('\n\n') if
                 passport_str.strip()]
    valid_passports = [passport for passport in passports if passport.is_valid()]
    print(f'There are {len(valid_passports)} out of {len(passports)} valid passports')


if __name__ == '__main__':
    main()
