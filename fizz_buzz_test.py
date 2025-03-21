from fizz_buzz import fizzBuzz

# test_fizz_buzz.py


def test_fizzbuzz_divisible_by_3_and_5():
    assert fizzBuzz(15) == "FizzBuzz"

def test_fizzbuzz_divisible_by_3_only():
    assert fizzBuzz(9) == "Fizz"

def test_fizzbuzz_divisible_by_5_only():
    assert fizzBuzz(10) == "Buzz"

def test_fizzbuzz_not_divisible_by_3_or_5():
    assert fizzBuzz(7) == 7