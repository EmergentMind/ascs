import random
import string

def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))

def random_year() -> int:
    return random.randrange(2025, 3000)
