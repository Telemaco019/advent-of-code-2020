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
        self.current_instruction_index = 0


class Instruction(metaclass=ABCMeta):
    def __init__(self, argument):
        self.executions_count = 0
        self.argument_sign = argument[0]
        self.argument_value = int(argument[1:])

    @abstractmethod
    def execute(self, state: ExecutionState):
        pass


class ChangeAccumulatorInstruction(Instruction):
    def __init__(self, argument):
        super().__init__(argument)

    def execute(self, state: ExecutionState):
        self.executions_count += 1
        if self.argument_sign == '+':
            state.accumulator += self.argument_value
        elif self.argument_sign == '-':
            state.accumulator -= self.argument_value


class NoOpInstruction(Instruction):
    def __init__(self, argument):
        super().__init__(argument)

    def execute(self, state: ExecutionState):
        self.executions_count += 1


class JumpInstruction(Instruction):
    def __init__(self, argument):
        super().__init__(argument)
        self.argument = argument

    def execute(self, state: ExecutionState):
        self.executions_count += 1
        if self.argument_sign == '+':
            state.current_instruction_index += self.argument_value
        elif self.argument_sign == '-':
            state.current_instruction_index -= self.argument_value


class Executor:
    def __init__(self, execution_state: ExecutionState):
        self.execution_state = execution_state

    def run(self):
        index = self.execution_state.current_instruction_index
        instruction = self.execution_state.instruction_list[index]
        if instruction.executions_count == 0:
            instruction.execute(self.execution_state)
            if self.execution_state.current_instruction_index == index:
                self.execution_state.current_instruction_index += 1
            self.run()


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


class PartOneTest(unittest.TestCase):
    def test_count(self):
        instruction_list = load_instructions(TEST_INPUT_FILE_NAME)
        state = ExecutionState(instruction_list)
        executor = Executor(state)
        executor.run()
        self.assertEqual(state.accumulator, 5)


def part_one():
    instruction_list = load_instructions(INPUT_FILE_NAME)
    state = ExecutionState(instruction_list)
    executor = Executor(state)
    executor.run()
    print(f'The value of the accumulator is {state.accumulator}')


def main():
    part_one()


if __name__ == '__main__':
    main()
    unittest.main()
