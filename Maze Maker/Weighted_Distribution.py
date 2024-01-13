import random
numbers = list(range(1, 11))  # Numbers from 1 to 10
def calc():

    weights = [10/i for i in numbers]

    chosen_number = random.choices(numbers, weights, k=1)[0]

    print(chosen_number)