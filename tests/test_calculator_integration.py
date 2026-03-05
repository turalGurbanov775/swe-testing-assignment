from src.calculator import Calculator

def test_full_flow_like_user_action():
    c = Calculator()
    start = c.clear()
    result = c.add(start, 5)
    assert result == 5

def test_clear_resets_to_zero():
    c = Calculator()
    c.current = 99
    assert c.clear() == 0