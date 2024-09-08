"""even number function"""
def is_even(number:int) -> bool:
    """this function is for detecting a number is even or not

    Args:
        number (int): number

    Returns:
        bool: True if even, False on number is odd
    """
    if number % 2 == 0:
        return True
    else:
        return False

def is_prime(number:int)-> bool:
    """this function finds number is prime or not

    Args:
        number (int): number
    
    Raises:
        ValueError: Input should not be less than 2.

    Returns:
        bool: True if prime, False if not
    """
    if number < 2:
        raise ValueError("Input should not be less than 2.")
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True
