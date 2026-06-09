import pytest

from lib.password_checker import PasswordChecker

def test_password_checker_raises_error_if_invalid():

    pw_checker = PasswordChecker()

    with pytest.raises(Exception) as e:
        pw_checker.check("qwerty")

    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."