from lib.counter import Counter

def test_counter_increases_by_num():

    counter = Counter()
    counter.add(4)
    result = counter.report()
    assert result == "Counted to 4 so far."