from lib.string_builder import StringBuilder

def test_string_builder_returns_input_string():

    stringbuilder = StringBuilder()
    stringbuilder.add("this is a test string")
    
    result = stringbuilder.output()

    assert result == "this is a test string"
    assert len(result) == stringbuilder.size()
