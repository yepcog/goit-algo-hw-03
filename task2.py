import random

def get_numbers_ticket(min=1, max=1000, quantity=6):
    unique = []
    unique = random.sample(range(min, max+1), quantity)
    unique.sort()
    return unique

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Winning lottery numbers:", lottery_numbers)