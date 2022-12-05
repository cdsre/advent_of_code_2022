from pytest import fixture, mark
from src.day_5 import get_initial_stacks, parse_move_instruction, get_move_instructions, process_move_instruction, \
    execute_crane_procedure, get_top_of_stacks, rearrange_and_get_top_stacks


@fixture()
def crane_procedure():
    return """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".splitlines()


@fixture(scope="function")
def stack_map():
    return {'1': ['Z', 'N'], '2': ['M', 'C', 'D'], '3': ['P']}


@fixture(scope="function")
def move_instructions():
    return ['move 1 from 2 to 1', 'move 3 from 1 to 3', 'move 2 from 2 to 1', 'move 1 from 1 to 2']


def test_get_initial_stacks(crane_procedure, stack_map):
    assert get_initial_stacks(crane_procedure) == stack_map


def test_parse_move_instruction():
    assert parse_move_instruction("move 1 from 2 to 1") == ['1', '2', '1']


def test_get_move_instructions(crane_procedure, move_instructions):
    assert get_move_instructions(crane_procedure) == move_instructions


@mark.parametrize("model,result", [
    (9000, {'1': ['Z', 'N'], '2': ['M'], '3': ['P', 'D', 'C']}),
    (9001, {'1': ['Z', 'N'], '2': ['M'], '3': ['P', 'C', 'D']})
])
def test_process_move_instruction(stack_map, model, result):
    process_move_instruction(stack_map, "2", "2", "3", model=model)
    assert stack_map == result


def test_execute_crane_procedure(stack_map, move_instructions):
    execute_crane_procedure(stack_map, move_instructions)
    assert stack_map == {'1': ['C'], '2': ['M'], '3': ['P', 'D', 'N', 'Z']}


def test_get_top_of_stacks(stack_map):
    assert get_top_of_stacks(stack_map) == ['N', 'D', 'P']


def test_rearrange_and_get_top_stacks(crane_procedure):
    assert rearrange_and_get_top_stacks(crane_procedure) == "CMZ"
