from lib.gratitudes import Gratitudes

def test_gratitude_returns_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("bacon")
    single_gratitude_result = gratitudes.format()
    assert single_gratitude_result == "Be grateful for: bacon"

    gratitudes.add("sunshine")
    gratitudes.add("kittens")
    multi_gratitude_result = gratitudes.format()
    assert multi_gratitude_result == "Be grateful for: bacon, sunshine, kittens"
    