import datetime
import pyautogui
import psutil

def random_number(seed=datetime.datetime.now().date(), seed_two=datetime.datetime(2010, 1, 1), return_int=True):
    number = 0
    seed_as_datetime = datetime.datetime(seed.year, seed.month, seed.day)
    date_diff = seed_as_datetime - seed_two
    date_as_secs = date_diff.total_seconds()
    mouseX, mouseY = pyautogui.position()
    process_count = 0
    for _ in psutil.process_iter():
        process_count += 1
    process_count_to_multiply = 0
    if process_count % 2 == 0:
        process_count_to_multiply = process_count * 2
    else:
        process_count_to_multiply = process_count * 3

    if mouseX > 0: date_as_secs *= 4
    if mouseY > 0: date_as_secs *= 2
    if mouseX < 0: date_as_secs *= 9
    if mouseY < 0: date_as_secs *= 8
    if (abs(mouseX + mouseY)) % 2 == 0: date_as_secs *= process_count_to_multiply*process_count
    if (abs(mouseX + mouseY)) % 2 != 0: date_as_secs *= process_count_to_multiply - process_count

    if return_int: number = int((date_as_secs / (abs(mouseX * mouseY))) * process_count_to_multiply)
    else: float((date_as_secs / (abs(mouseX * mouseY))) * process_count_to_multiply)
    return number

def random_range(min, max_excl, return_int=True):
    if return_int: number = random_number(return_int=True) % max_excl
    else: number = random_number(return_int=False) % max_excl
    if number < max_excl - min: number += min

    if return_int: return int(number)
    else: return float(number)

def random_choice(*args):
    length = 0
    for _ in args: length += 1 
    rand = random_range(0, length)
    return args[rand]

def random_choice_arr(choices_array):
    length = 0
    for _ in choices_array: length += 1 
    rand = random_range(0, length)
    return choices_array[rand]
