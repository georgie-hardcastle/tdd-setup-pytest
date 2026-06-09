
import pytest

from lib.present import Present

def test_present_throws_error_if_present_already_wrapped():
    present = Present()
    present.contents = "a new guitar"

    with pytest.raises(Exception) as e:
        present.wrap("a knitted jumper")
    
    error_message = str(e.value)
    assert error_message == "A present has already been wrapped."

def test_present_throws_error_if_no_presents_wrapped():
    present = Present()

    with pytest.raises(Exception) as e:
        present.unwrap()
    
    error_message = str(e.value)
    assert error_message == "No presents have been wrapped."