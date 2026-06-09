from lib.check_codeword import check_codeword

def test_check_codeword_returns_correct_for_horse():

    result = check_codeword("horse")

    assert result == "Correct! Come in."

def test_check_codeword_returns_close_for_almost_correct():

    result = check_codeword("hearse")

    assert result == "Close, but nope."

def test_check_codeword_returns_wrong_for_incorrect():

    result = check_codeword("cat")

    assert result == "WRONG!"