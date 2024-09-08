"""__Demo on exception_handling on calling a function"""
from src.finance.calculator import is_prime
# It helps the program run smoothly, on passing error-causing arguments
# without abruptly stopping with an error
try:
    RESULT = is_prime(0)
    print(RESULT)
except ValueError as e:
    print(f"error:{e}")
    # We can aslo pass other error#
# except TypeError as e:
#     print(f"TypeError: {e}")
