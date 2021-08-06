def near_ten(num):
    remainder = num % 10
    if remainder == 1 or remainder == 2 or remainder == 0 or remainder == 8 or remainder == 9:
        return True
    else:
        return False
