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

# Additional test cases
def test_fizzbuzz_zero():
    assert fizzBuzz(0) == "FizzBuzz"  # 0 is divisible by both 3 and 5

def test_fizzbuzz_negative_divisible_by_3_and_5():
    assert fizzBuzz(-15) == "FizzBuzz"

def test_fizzbuzz_negative_divisible_by_3_only():
    assert fizzBuzz(-9) == "Fizz"

def test_fizzbuzz_negative_divisible_by_5_only():
    assert fizzBuzz(-10) == "Buzz"

def test_fizzbuzz_negative_not_divisible_by_3_or_5():
    assert fizzBuzz(-7) == -7

def test_fizzbuzz_large_number():
    assert fizzBuzz(150) == "FizzBuzz"  # Large number divisible by 3 and 5

def test_fizzbuzz_large_prime():
    assert fizzBuzz(101) == 101  # Prime number not divisible by 3 or 5