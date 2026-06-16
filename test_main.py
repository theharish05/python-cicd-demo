from main import fibonacci

def test_fib_0():
    assert fibonacci(0) == 0

def test_fib_1():
    assert fibonacci(1) == 1

def test_fib_2():
    assert fibonacci(2) == 1

def test_fib_3():
    assert fibonacci(3) == 2

def test_fib_4():
    assert fibonacci(4) == 3

def test_fib_5():
    assert fibonacci(5) == 5

def test_fib_6():
    assert fibonacci(6) == 8

def test_fib_7():
    assert fibonacci(7) == 13

def test_fib_8():
    assert fibonacci(8) == 21

def test_fib_10():
    assert fibonacci(10) == 55
