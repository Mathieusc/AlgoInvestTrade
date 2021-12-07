from itertools import combinations
from timeit import timeit
from time import time

start_time = time()

# Data : (Cost in €, Profit in %)
actions = [
    (20, 5),
    (30, 10),
    (50, 15),
    (70, 20),
    (60, 17),
    (80, 25),
    (22, 7),
    (26, 11),
    (48, 13),
    (34, 27),
    (42, 17),
    (110, 9),
    (38, 23),
    (14, 1),
    (18, 3),
    (8, 8),
    (4, 12),
    (10, 14),
    (24, 21),
    (114, 18)
]

# Create a list of action cost.
action_cost_list = [action[0] for action in actions]
# Associate each action cost to their profit in euros in a dictionary.
action_profit = {action[0]: (action[0] * action[1]) / 100 for action in actions}



def bruteforce(action, profit):
    results = []
    for i in range(1, len(action)):
        action_combinations = combinations(action, i)
        actions_profit_list = []
        for action_combination in action_combinations:
            if sum(action_combination) <= 500:
                actions_profit_list.append((action_combination, sum([profit[action] for action in action_combination])))
        results += actions_profit_list

    return max(results, key = lambda x: x[1])


def execution_time(start, end):
    execution_time = end_time - start_time
    display_execution_time = f"The bruteforce method took {execution_time:.2f} seconds."
    print(display_execution_time)

find_best_profit = bruteforce(action_cost_list, action_profit)

end_time = time()
execution_time(start_time, end_time)

# To use the timeit module instead uncomment this
# Timeit() seems to be more precise than time()
# bruteforce_time = timeit(lambda: bruteforce(action_cost_list, action_profit), number=1)
# print(f"bruteforce = {bruteforce_time:.3f}")