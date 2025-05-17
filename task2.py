import random

def get_numbers_ticket(min, max, quantity):
    result = []
    try:
        random.sample(range(min, max+1), quantity)
    except ValueError:
        return result
    else:
        if min < 1 or max > 1000:
            return result
        else:
            result = random.sample(range(min, max+1), quantity)
            result.sort()
            return result

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Winning lottery numbers:", lottery_numbers)