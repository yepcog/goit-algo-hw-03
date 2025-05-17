import re

def normalize_phone(phone_number):
    phone_number.strip()
    clean_number = re.sub("[^0-9]", "", phone_number)
    try:
        clean_number.index("38") == 0
    except ValueError:
        result = "+38" + clean_number
        return result
    else:
        result = "+" + clean_number
        return result

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers:", sanitized_numbers)