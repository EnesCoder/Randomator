from randomator import *

random_num = random_number()
print(random_num)

random_rng = random_range(0, 9)
print(random_rng)

random_chc = random_choice("I", "Love", "Piza")
print(random_chc)

arr = ["I", "Hate", "Pineapple", "Piza"]
random_chc_arr = random_choice_arr(arr)
print(random_chc_arr)
