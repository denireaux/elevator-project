from src.elevator_core import core_elevator_logic

def test_provided_example():
    """Validates the math from the project prompt."""
    time, path = core_elevator_logic(12, [2, 9, 1, 32])
    assert time == 560
    assert path == [12, 2, 9, 1, 32]

def test_elevator_stays_put():
    """Checks that time doesn't increase if floor doesn't change."""
    time, path = core_elevator_logic(5, [5])
    assert time == 0
    assert path == [5, 5]

def test_back_and_forth():
    """Checks travel logic when changing directions multiple times."""
    time, path = core_elevator_logic(10, [20, 10])
    assert time == 200
    assert path == [10, 20, 10]

def test_empty_floors_list():
    """Ensures the system doesn't crash if no floors are provided."""
    time, path = core_elevator_logic(10, [])
    assert time == 0
    assert path == [10]
