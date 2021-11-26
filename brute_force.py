# Brute force algorithms to check :
# SSS*, AlphaBeta, MinMax, A*, BackTrack, BackJump, BackMark, NC-AC(n), ForwardChecking…

import itertools
import timeit
import time

# Data :
actions = {
    20: 5,
    30: 10,
    50: 15,
    70: 20,
    60: 17,
    80: 25,
    22: 7,
    26: 11,
    48: 13,
    34: 27,
    42: 17,
    110: 9,
    38: 23,
    14: 1,
    18: 3,
    8: 8,
    4: 12,
    10: 14,
    24: 21,
    114: 18
    }


def calculate_profit(actions):
    """
    param: {dict} of action costs in € and profits in %.
    return: dict of profit per actions in €.
    """
    profit = {}
    for action, percent in actions.items():
        profit[action] =  action * percent / 100

    return profit

profit = calculate_profit(actions)

# Seperating action costs and profit into individual lists.
action_cost = [action for action in profit.keys()]
profit = [profit for profit in profit.values()]


def try_all_combinations(action_list, profit_list):
    """
    Compare each profit and it's costs and map them into a dictionary.

    Return:
        List of dict.
    """

    # Initialize dict for mapping.
    results = create_dict(len(action_list))

    start = time.time()

    for i in range(len(action_list) + 1):
        action_combination = itertools.combinations(action_list, i)
        results[i]["actions"] = [result for result in action_combination]

    for i in range(len(profit_list) + 1):
        profit_combination = itertools.combinations(profit_list, i)
        results[i]["profit"] = [sum(result) for result in profit_combination]

    end = time.time()
    print(f"time: {end - start} seconds.")

    return results

def create_dict(actions):
    """
    Setup empty dict for each actions.

    Return:
        List of dict with empty values for actions and profit.
    """
    combinations = {"actions": None, "profit": None}
    results = []

    for i in range(actions + 1):
        all_combinations = combinations.copy()
        results.append(all_combinations)

    return results

combinations = try_all_combinations(action_cost, profit)

# total = 0
# Total = [total := total + x for x in action_cost]
# print(Total)

print(combinations[10]["actions"][0])
print(combinations[10]["profit"][0])

# Find best profit next !