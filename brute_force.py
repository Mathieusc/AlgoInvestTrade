from itertools import combinations
import timeit
from time import time

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


def calculate_profit_euros(actions):
    """
    Param: 
        Dict of action costs in € and profits in %.
    Return: 
        Dict of profit per actions in €.
    """
    profit = {}

    for action, percent in actions.items():
        profit[action] =  action * percent / 100

    return profit


def find_best_result(actions):
    """
    Param:
        List of dict of the combinations of actions in €
        and their profits in €.
    Return:
        List of dict.
    """
    
    # Ugly af
    actions.pop()
    actions.pop()
    actions.pop()
    actions.pop()
    del actions[0]
    print(actions)
    for d in actions:
        print(max(d["profit"]))
        best_profit = max(d["profit"])
        #print([key for (key, value) in d.items() if value == best_profit])
        # I need to find the index of that max value since I have 2 dicts...
        # Maybe convert the 2 dicts into a list and access the key by the index of the best value...


#profit = calculate_profit_euros(actions)

# Seperating action costs and profit into individual lists.
action_cost = [action for action in actions.keys()]
profit = [profit for profit in actions.values()]


def try_all_combinations(action_list, profit_list):
    """
    Compare each profit and it's costs and map them into a dictionary.

    Return:
        List of dict.
    """

    # Initialize dict for mapping.
    results = create_dict(len(action_list))

    start = time()

    for i in range(1, len(action_list) - 3):
        action_combination = combinations(action_list, i)
        results[i]["actions"] = [result for result in action_combination]

        profit_combination = combinations(profit_list, i)
        #print([x for x in profit_combination])
        # Percent
        #results[i]["profit"] = [sum(result) * 100 / sum(results[i]["actions"][n]) for n, result in enumerate(profit_combination)]
        
        # Return on invest (not accurate)
        #results[i]["profit"] = [(sum(result) - sum(results[i]["actions"][n])) / sum(results[i]["actions"][n]) for n, result in enumerate(profit_combination)]
        
        # Profit in euros (what we need ?)
        # Max value * Profit % // 100
        results[i]["profit"] = [(sum(results[i]["actions"][n]) * sum(result)) / 100 for n, result in enumerate(profit_combination)]

    end = time()
    print(f"time: {end - start} seconds.")

    return results

def create_dict(actions):
    """
    Setup empty dict for each actions.

    Return:
        List of dict with empty values for actions and profit. 
    """
    combinations = {"actions": "", "profit": ""}
    results = []

    for i in range(actions + 1):
        all_combinations = combinations.copy()
        results.append(all_combinations)

    return results

combinations = try_all_combinations(action_cost, profit)
best_invest = find_best_result(combinations)