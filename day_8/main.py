import unittest
from abc import ABCMeta, abstractmethod

INPUT_FILE_NAME = 'input.txt'
TEST_INPUT_FILE_NAME = 'input_test.txt'

INSTRUCTION_ACC = 'acc'
INSTRUCTION_NOP = 'nop'
INSTRUCTION_JUMP = 'jmp'


def load_file_lines(file_name):
    with open(file_name) as file:
        return file.readlines()


class ExecutionState:
    def __init__(self, instruction_list: list):
        self.accumulator = 0
        self.instruction_list = instruction_list


class Instruction(metaclass=ABCMeta):
    def __init__(self):
        self.executions_count = 0

    @abstractmethod
    def execute(self, state: ExecutionState) -> ExecutionState:
        self.executions_count += 1


class ChangeAccumulatorInstruction(Instruction):
    def __init__(self, argument):
        super().__init__()

    def execute(self, state: ExecutionState) -> ExecutionState:
        super().execute(state)


class NoOpInstruction(Instruction):
    def __init__(self, argument):
        super().__init__()

    def execute(self, state: ExecutionState) -> ExecutionState:
        super().execute(state)


class JumpInstruction(Instruction):
    def __init__(self, argument):
        super().__init__()
        self.argument = argument

    def execute(self, state: ExecutionState) -> ExecutionState:
        super().execute(state)
        pass


class InstructionFactory:
    def __init__(self):
        pass

    @staticmethod
    def from_instruction_name(instruction_name, instruction_arg):
        if INSTRUCTION_ACC == instruction_name:
            return ChangeAccumulatorInstruction(instruction_arg)
        elif INSTRUCTION_JUMP == instruction_name:
            return JumpInstruction(instruction_arg)
        elif INSTRUCTION_NOP == instruction_name:
            return NoOpInstruction(instruction_arg)
        else:
            raise Exception(f'Instruction name {instruction_name} is not valid')


def load_instructions(file_name):
    lines = load_file_lines(file_name)
    return [InstructionFactory.from_instruction_name(*line.split(' ')) for line in lines]


def main():
    instruction_list = load_instructions(TEST_INPUT_FILE_NAME)
    state = ExecutionState(instruction_list)


if __name__ == '__main__':
    main()
    unittest.main()
