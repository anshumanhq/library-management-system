import random
from datetime import date
import json
import os

def generate_id(prefix):
    return prefix + ''.join(str(random.randint(0, 9)) for _ in range(3))

def validate_isbn(isbn):
    isbn = isbn.replace("-", "").replace(" ", "")
    
    # ISBN-10
    if len(isbn) == 10:
        if not isbn[:9].isdigit():
            return False
        total = 0
        for i in range(9):
            total += int(isbn[i]) * (10 - i)
        check = 10 if isbn[9] == 'X' else int(isbn[9])
        total += check
        return total % 11 == 0
    
    # ISBN-13
    elif len(isbn) == 13:
        if not isbn[:12].isdigit():
            return False
        total = 0
        for i in range(12):
            digit = int(isbn[i])
            total += digit * (1 if i % 2 == 0 else 3)
        check_digit = (10 - (total % 10)) % 10
        return check_digit == int(isbn[12])
    
    return False

def get_current_date():
    return date.today().strftime("%Y-%m-%d")

def load_data(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(file_path, data_list):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(data_list, f, indent=4)
    return True